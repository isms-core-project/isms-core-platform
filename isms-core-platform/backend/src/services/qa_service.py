"""QA / Correlation Engine — Phase 5.

Phase 5.1: Existence Checker
  For each control group, verifies that required artefacts exist:
    Framework : POL + UG + TG + Assessment
    Operational: OP-POL + Assessment (skip foundation group "00")

Phase 5.2: Keyword Correlation
  Extracts keywords from ISO 27001 control titles/descriptions, then checks
  whether those keywords appear in the implementation content (UG+TG) stored
  in OpenSearch. Scores 0–1, thresholds: PASS ≥0.60, WARNING ≥0.35, FAIL <0.35.

Results are written to the correlation_results table.
Each run replaces the previous results for the given method.
"""
import logging
import re
import time
import uuid
from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import CorrelationMethod, ProductFamily, ProductType, QAStatus
from src.database.session import engine
from src.domain.assessments import Assessment
from src.domain.content import Implementation, Policy
from src.domain.control_groups import ControlGroup
from src.domain.frameworks import Framework, FrameworkControl
from src.domain.qa import Base, CorrelationResult, SynonymRule
from src.services import search_service

logger = logging.getLogger(__name__)

# Artefact keys used in coverage_keywords / missing_keywords arrays
_FW_KEYS = ["policy", "UG", "TG", "assessment"]
_OP_KEYS = ["policy", "assessment"]

# Foundation group excluded from operational checks
_FOUNDATION_CODE = "00"

# ── Phase 5.2: keyword extraction ────────────────────────────────────────────

_STOP_WORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "on", "with",
    "that", "this", "is", "are", "be", "been", "by", "from", "at", "as",
    "its", "it", "all", "such", "any", "which", "where", "when", "who",
    "not", "use", "used", "using", "should", "shall", "must", "may", "can",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "within", "across", "about", "between", "than", "more", "also", "other",
    "their", "they", "them", "these", "those", "each", "into", "over",
    "been", "both", "being", "through", "during", "only", "own", "same",
}

_KW_PASS_THRESHOLD = Decimal("0.60")
_KW_WARN_THRESHOLD = Decimal("0.35")

# Synonym weight — synonym match counts less than an exact match
_KW_SYNONYM_WEIGHT = Decimal("0.7")

# Suffix stripping for stem matching (longest first so we strip greedily)
_STEM_SUFFIXES = (
    "mentation", "isation", "ization", "ification",
    "ations", "ments", "tions", "sions",
    "ness", "ance", "ence", "ment", "tion", "sion",
    "ings", "ated", "ates", "ical", "able", "ible", "ally",
    "ful", "less", "ing", "ity",
    "ers", "ied", "ies", "ed", "er", "ly", "al", "es",
)
_MIN_STEM_LEN = 4


def _stem(word: str) -> str:
    """Strip the longest known suffix to produce a matchable stem.

    e.g. management → manage, monitoring → monitor, addressing → address
    """
    for suffix in _STEM_SUFFIXES:
        if word.endswith(suffix) and (len(word) - len(suffix)) >= _MIN_STEM_LEN:
            return word[: -len(suffix)]
    return word

# ISMS-specific synonym dictionary.
# Key = ISO keyword that may be extracted; values = equivalent terms
# that carry the same meaning in information security documentation.
_SYNONYMS: dict[str, list[str]] = {
    # ── Action verbs ──────────────────────────────────────────────────────────
    "addressing":     ["handling", "managing", "treating", "mitigating", "dealing"],
    "ensuring":       ["guaranteeing", "maintaining", "verifying", "confirming", "assuring"],
    "protecting":     ["safeguarding", "securing", "defending", "preserving"],
    "monitoring":     ["tracking", "reviewing", "auditing", "observing", "supervising"],
    "implementing":   ["applying", "deploying", "establishing", "executing", "enforcing"],
    "reviewing":      ["assessing", "evaluating", "auditing", "checking", "examining"],
    "identifying":    ["detecting", "recognising", "discovering", "finding"],
    "controlling":    ["managing", "governing", "regulating", "overseeing"],
    "managing":       ["controlling", "overseeing", "administering", "governing", "handling"],
    "establishing":   ["creating", "defining", "setting", "implementing", "forming"],
    "maintaining":    ["sustaining", "keeping", "preserving", "upholding"],
    "preventing":     ["avoiding", "stopping", "blocking", "mitigating", "deterring"],
    "detecting":      ["identifying", "finding", "discovering", "recognising"],
    "responding":     ["reacting", "handling", "addressing", "managing"],
    "reporting":      ["documenting", "recording", "notifying", "disclosing"],
    "documenting":    ["recording", "logging", "tracking", "capturing"],
    "classifying":    ["categorising", "labelling", "tagging", "marking"],
    "encrypting":     ["encoding", "protecting", "ciphering", "cryptographic"],
    "authenticating": ["verifying", "validating", "confirming"],
    "authorising":    ["permitting", "allowing", "granting", "approving"],
    "disposing":      ["deleting", "destroying", "erasing", "purging", "removing"],
    "segregating":    ["separating", "isolating", "partitioning", "dividing"],
    "hardening":      ["securing", "configuring", "locking", "restricting"],
    # ── Security nouns ────────────────────────────────────────────────────────
    "threats":        ["risks", "vulnerabilities", "dangers", "hazards", "attacks"],
    "vulnerabilities":["weaknesses", "flaws", "gaps", "exposures", "risks"],
    "incidents":      ["events", "breaches", "occurrences", "issues", "problems"],
    "assets":         ["resources", "systems", "data", "equipment", "components"],
    "personnel":      ["staff", "employees", "users", "workforce", "people"],
    "suppliers":      ["vendors", "contractors", "providers", "third-parties"],
    "requirements":   ["obligations", "standards", "criteria", "specifications"],
    "procedures":     ["processes", "methods", "instructions", "guidelines"],
    "controls":       ["measures", "safeguards", "mechanisms", "countermeasures"],
    "disclosure":     ["reporting", "notification", "communication", "sharing"],
    "deletion":       ["removal", "erasure", "purging", "destruction", "wiping"],
    "retention":      ["storage", "keeping", "preservation", "archiving"],
    "transfer":       ["transmission", "sharing", "exchange", "movement"],
    "testing":        ["verification", "validation", "assessment", "evaluation"],
    "logging":        ["recording", "auditing", "tracking", "monitoring"],
    "patching":       ["updating", "fixing", "remediation", "maintenance"],
    "encryption":     ["cryptography", "ciphering", "encoding", "protection"],
    "authentication": ["verification", "validation", "identity", "login"],
    "authorisation":  ["permission", "access", "privilege", "rights"],
    "classification": ["categorisation", "labelling", "marking", "tagging"],
    "segregation":    ["separation", "isolation", "partitioning", "division"],
}


def ensure_synonym_table() -> None:
    """Create synonym_rules table if absent, then seed from _SYNONYMS defaults."""
    # Create only the synonym_rules table (checkfirst=True skips if exists)
    SynonymRule.__table__.create(bind=engine, checkfirst=True)

    # Seed hardcoded defaults if table is empty
    with engine.begin() as conn:
        from sqlalchemy import text as sa_text
        count = conn.execute(sa_text("SELECT COUNT(*) FROM synonym_rules")).scalar()
        if count == 0:
            rows = [
                {"id": uuid.uuid4(), "keyword": kw, "synonyms": syns}
                for kw, syns in _SYNONYMS.items()
            ]
            conn.execute(
                SynonymRule.__table__.insert(),
                rows,
            )
            logger.info("Seeded %d synonym rules from defaults", len(rows))


def load_synonyms(db: DBSession) -> dict[str, list[str]]:
    """Load synonym rules from DB, falling back to hardcoded defaults."""
    try:
        rows = db.execute(select(SynonymRule)).scalars().all()
        if rows:
            return {r.keyword: list(r.synonyms) for r in rows}
    except Exception as e:
        logger.warning("Could not load synonyms from DB, using defaults: %s", e)
    return dict(_SYNONYMS)


def _extract_keywords(text: str, max_kw: int = 15) -> list[str]:
    """Extract meaningful keywords from ISO control title/description text."""
    tokens = re.findall(r'\b[a-z]{4,}\b', text.lower())
    seen: set[str] = set()
    keywords: list[str] = []
    for token in tokens:
        if token not in _STOP_WORDS and token not in seen:
            seen.add(token)
            keywords.append(token)
            if len(keywords) >= max_kw:
                break
    return keywords


def _kw_status(strength: Decimal) -> QAStatus:
    if strength >= _KW_PASS_THRESHOLD:
        return QAStatus.PASS
    if strength >= _KW_WARN_THRESHOLD:
        return QAStatus.WARNING
    return QAStatus.FAIL


def _fetch_group_full_text(os_client, group_code: str, language: str = "en") -> str:
    """Fetch concatenated full_text from OpenSearch for a control group.

    Uses a prefix query so that a DB code like 'a.5.1-2' matches documents
    indexed as 'a.5.1-2-6.1-2' (stacked multi-section groups).
    Filters to the specified language (default 'en').
    """
    try:
        query: dict = {
            "bool": {
                "must": [
                    {"prefix": {"control_group_code": group_code.lower()}},
                ],
                "filter": [
                    {"term": {"language": language}},
                ],
            }
        }
        result = os_client.search(
            index=search_service.IDX_IMPLEMENTATIONS,
            body={
                "query": query,
                "_source": ["full_text"],
                "size": 20,
            },
        )
        parts = [
            hit["_source"].get("full_text", "")
            for hit in result["hits"]["hits"]
        ]
        return " ".join(parts).lower()
    except Exception as e:
        logger.warning("OpenSearch fetch failed for group %s: %s", group_code, e)
        return ""


def _fw_status(present: list[str]) -> QAStatus:
    n = len(present)
    if n == 4:
        return QAStatus.PASS
    has_pol = "policy" in present
    has_ass = "assessment" in present
    has_guide = "UG" in present or "TG" in present
    if has_pol and has_ass and has_guide:
        return QAStatus.WARNING   # missing one guide
    if n == 0:
        return QAStatus.NEEDS_REVIEW
    return QAStatus.FAIL


def _op_status(present: list[str]) -> QAStatus:
    n = len(present)
    if n == 2:
        return QAStatus.PASS
    if n == 1:
        return QAStatus.WARNING
    return QAStatus.FAIL


def run_existence_check(
    db: DBSession,
    group_id: uuid.UUID | None = None,
) -> dict:
    """Run the existence check for all (or one) control groups.

    Deletes previous EXISTENCE results before writing fresh ones.
    Returns a summary dict with counts and duration.
    """
    t0 = time.monotonic()
    run_date = datetime.now(timezone.utc)

    # Load control groups
    q = select(ControlGroup).order_by(ControlGroup.group_code)
    if group_id:
        q = q.where(ControlGroup.id == group_id)
    groups = db.execute(q).scalars().all()

    # Drop previous existence results for the scope
    del_q = delete(CorrelationResult).where(
        CorrelationResult.correlation_method == CorrelationMethod.EXISTENCE
    )
    if group_id:
        del_q = del_q.where(CorrelationResult.control_group_id == group_id)
    db.execute(del_q)

    stats: dict[str, int] = {
        "total": 0,
        "pass": 0,
        "warning": 0,
        "fail": 0,
        "needs_review": 0,
    }

    for group in groups:
        # ── Fetch artefact values (.value gives the actual string e.g. "OP-POL") ──
        pol_rows = db.execute(
            select(Policy.policy_type, Policy.product_type, Policy.source_label).where(
                Policy.control_group_id == group.id
            )
        ).all()
        pol_types: list[str] = [r[0].value for r in pol_rows]
        impl_types: list[str] = [
            i.value for i in db.execute(
                select(Implementation.impl_type).where(
                    Implementation.control_group_id == group.id
                )
            ).scalars().all()
        ]
        fw_assessments: int = db.scalar(
            select(func.count()).select_from(Assessment).where(
                Assessment.control_group_id == group.id,
                Assessment.product_type == ProductType.FRAMEWORK,
            )
        ) or 0
        op_assessments: int = db.scalar(
            select(func.count()).select_from(Assessment).where(
                Assessment.control_group_id == group.id,
                Assessment.product_type == ProductType.OPERATIONAL,
            )
        ) or 0

        # External docs for this group (source_label list for annotation)
        external_sources: list[str] = [
            r[2] or "unknown"
            for r in pol_rows
            if r[1] == ProductType.EXTERNAL
        ]
        has_external = len(external_sources) > 0

        # ── PRIVACY / CLOUD: simple policy-existence check ───────────────────
        if group.product_family in (ProductFamily.PRIVACY, ProductFamily.CLOUD):
            expected_pt = (
                ProductType.PRIVACY
                if group.product_family == ProductFamily.PRIVACY
                else ProductType.CLOUD
            )
            has_native_pol = any(r[1] == expected_pt for r in pol_rows)
            pf_label = group.product_family.value.lower()
            pf_present = ["policy"] if has_native_pol else []
            pf_missing = [] if has_native_pol else ["policy"]
            pf_strength = Decimal("1") if has_native_pol else Decimal("0")
            pf_status = QAStatus.PASS if has_native_pol else QAStatus.FAIL
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=f"{group.group_code}:{pf_label}",
                correlation_method=CorrelationMethod.EXISTENCE,
                correlation_strength=pf_strength,
                qa_status=pf_status,
                coverage_keywords=pf_present,
                missing_keywords=pf_missing,
                run_date=run_date,
                metadata_={
                    "product_type": pf_label,
                    "has_pol": has_native_pol,
                    "pol_count": sum(1 for r in pol_rows if r[1] == expected_pt),
                },
            ))
            stats["total"] += 1
            stats[pf_status.value] += 1
            continue  # skip ISMS fw/op checks

        # ── Framework check ──────────────────────────────────────────────────
        has_pol = "POL" in pol_types
        has_ug = "UG" in impl_types
        has_tg = "TG" in impl_types
        has_fw_ass = fw_assessments > 0

        fw_present = [k for k, v in zip(_FW_KEYS, [has_pol, has_ug, has_tg, has_fw_ass]) if v]
        fw_missing = [k for k, v in zip(_FW_KEYS, [has_pol, has_ug, has_tg, has_fw_ass]) if not v]
        fw_strength = Decimal(len(fw_present)) / Decimal(4)
        # If no native POL but an external doc covers the group: cap at WARNING
        fw_status = _fw_status(fw_present)
        if not has_pol and has_external and fw_status == QAStatus.FAIL:
            fw_status = QAStatus.WARNING

        db.add(CorrelationResult(
            control_group_id=group.id,
            document_id=f"{group.group_code}:fw",
            correlation_method=CorrelationMethod.EXISTENCE,
            correlation_strength=fw_strength,
            qa_status=fw_status,
            coverage_keywords=fw_present,
            missing_keywords=fw_missing,
            run_date=run_date,
            metadata_={
                "product_type": "framework",
                "has_pol": has_pol,
                "has_ug": has_ug,
                "has_tg": has_tg,
                "has_assessment": has_fw_ass,
                "pol_count": pol_types.count("POL"),
                "ug_count": impl_types.count("UG"),
                "tg_count": impl_types.count("TG"),
                "assessment_count": fw_assessments,
                "has_external": has_external,
                "external_sources": external_sources,
            },
        ))
        stats["total"] += 1
        stats[fw_status.value] += 1

        # ── Operational check (skip foundation group "00") ───────────────────
        if group.group_code != _FOUNDATION_CODE:
            has_op_pol = "OP-POL" in pol_types
            has_op_ass = op_assessments > 0

            op_present = [k for k, v in zip(_OP_KEYS, [has_op_pol, has_op_ass]) if v]
            op_missing = [k for k, v in zip(_OP_KEYS, [has_op_pol, has_op_ass]) if not v]
            op_strength = Decimal(len(op_present)) / Decimal(2)
            op_status = _op_status(op_present)

            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=f"{group.group_code}:op",
                correlation_method=CorrelationMethod.EXISTENCE,
                correlation_strength=op_strength,
                qa_status=op_status,
                coverage_keywords=op_present,
                missing_keywords=op_missing,
                run_date=run_date,
                metadata_={
                    "product_type": "operational",
                    "has_op_pol": has_op_pol,
                    "has_assessment": has_op_ass,
                    "op_pol_count": pol_types.count("OP-POL"),
                    "assessment_count": op_assessments,
                },
            ))
            stats["total"] += 1
            stats[op_status.value] += 1

    db.commit()
    stats["duration_ms"] = int((time.monotonic() - t0) * 1000)
    logger.info("Existence check complete: %s", stats)
    return stats


def run_keyword_check(
    db: DBSession,
    group_id: uuid.UUID | None = None,
) -> dict:
    """Run keyword correlation for all (or one) control groups.

    Extracts keywords from the ISO 27001 control titles/descriptions that each
    control group maps to, then checks whether those keywords appear in the
    implementation content stored in OpenSearch.

    Deletes previous KEYWORD results before writing fresh ones.
    Returns a summary dict with counts and duration.
    """
    t0 = time.monotonic()
    run_date = datetime.now(timezone.utc)

    os_client = search_service.get_client()
    os_available = os_client is not None
    if not os_available:
        logger.warning("OpenSearch unavailable — keyword check will mark all as needs_review")

    # Load synonym rules from DB (falls back to hardcoded defaults)
    synonyms = load_synonyms(db)

    # Load all control groups (ISMS + Privacy + Cloud)
    q = select(ControlGroup).order_by(ControlGroup.group_code)
    if group_id:
        q = q.where(ControlGroup.id == group_id)
    groups = db.execute(q).scalars().all()

    # Load frameworks for keyword source — one per product family
    _framework_codes = {
        ProductFamily.ISMS: "ISO27001_2022",
        ProductFamily.PRIVACY: "ISO27701",
        ProductFamily.CLOUD: "ISO27018",
    }
    frameworks = {
        family: db.execute(
            select(Framework).where(Framework.code == code)
        ).scalar_one_or_none()
        for family, code in _framework_codes.items()
    }

    # Drop previous keyword results for the scope
    del_q = delete(CorrelationResult).where(
        CorrelationResult.correlation_method == CorrelationMethod.KEYWORD
    )
    if group_id:
        del_q = del_q.where(CorrelationResult.control_group_id == group_id)
    db.execute(del_q)

    stats: dict[str, int] = {
        "total": 0,
        "pass": 0,
        "warning": 0,
        "fail": 0,
        "needs_review": 0,
    }

    for group in groups:
        doc_id = f"{group.group_code}:kw"
        control_ids: list[str] = group.stacked_control_ids or []
        framework = frameworks.get(group.product_family)
        product_label = group.product_family.value.lower() if group.product_family else "isms"

        # ── Build keyword corpus from ISO control titles/descriptions ─────────
        if framework and control_ids:
            fw_controls = db.execute(
                select(FrameworkControl).where(
                    FrameworkControl.framework_id == framework.id,
                    FrameworkControl.control_id.in_(control_ids),
                )
            ).scalars().all()
            corpus = " ".join(
                f"{fc.title} {fc.description or ''}" for fc in fw_controls
            )
        else:
            corpus = group.name  # fallback: group name as keyword source

        keywords = _extract_keywords(corpus)

        # ── No keywords → NEEDS_REVIEW ────────────────────────────────────────
        if not keywords:
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=doc_id,
                correlation_method=CorrelationMethod.KEYWORD,
                correlation_strength=Decimal("0"),
                qa_status=QAStatus.NEEDS_REVIEW,
                coverage_keywords=[],
                missing_keywords=[],
                run_date=run_date,
                metadata_={"product_type": product_label, "reason": "no_keywords_extracted", "control_ids": control_ids},
            ))
            stats["total"] += 1
            stats["needs_review"] += 1
            continue

        # ── OpenSearch unavailable → NEEDS_REVIEW ────────────────────────────
        if not os_available:
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=doc_id,
                correlation_method=CorrelationMethod.KEYWORD,
                correlation_strength=Decimal("0"),
                qa_status=QAStatus.NEEDS_REVIEW,
                coverage_keywords=[],
                missing_keywords=keywords,
                run_date=run_date,
                metadata_={"product_type": product_label, "reason": "opensearch_unavailable", "keywords": keywords},
            ))
            stats["total"] += 1
            stats["needs_review"] += 1
            continue

        # ── Keyword matching against OpenSearch content (English primary) ────
        full_text = _fetch_group_full_text(os_client, group.group_code, language="en")

        found_exact: list[str] = []
        synonym_matches: dict[str, str] = {}   # {keyword: synonym_used}
        missing: list[str] = []

        for kw in keywords:
            if kw in full_text:
                found_exact.append(kw)
            else:
                # Stem match: "management" → "manage", counts as exact
                kw_stem = _stem(kw)
                if kw_stem != kw and kw_stem in full_text:
                    found_exact.append(kw)
                else:
                    # Synonym match: different word, counts at 0.7×
                    syn_hit = next(
                        (s for s in synonyms.get(kw, []) if s in full_text),
                        None,
                    )
                    if syn_hit:
                        synonym_matches[kw] = syn_hit
                    else:
                        missing.append(kw)

        n = len(keywords)
        weighted = Decimal(len(found_exact)) + Decimal(len(synonym_matches)) * _KW_SYNONYM_WEIGHT
        strength = weighted / Decimal(n) if n else Decimal("0")
        # If no OS content exists yet, mark NEEDS_REVIEW rather than FAIL
        status = _kw_status(strength) if full_text else QAStatus.NEEDS_REVIEW

        db.add(CorrelationResult(
            control_group_id=group.id,
            document_id=doc_id,
            correlation_method=CorrelationMethod.KEYWORD,
            correlation_strength=strength,
            qa_status=status,
            coverage_keywords=found_exact,
            missing_keywords=missing,
            run_date=run_date,
            metadata_={
                "product_type": product_label,
                "language": "en",
                "total_keywords": n,
                "found_exact": len(found_exact),
                "found_synonym": len(synonym_matches),
                "synonym_matches": synonym_matches,
                "control_ids": control_ids,
                "has_os_content": bool(full_text),
            },
        ))
        stats["total"] += 1
        stats[status.value] += 1

    db.commit()
    stats["duration_ms"] = int((time.monotonic() - t0) * 1000)
    logger.info("Keyword check complete: %s", stats)
    return stats


# ── Phase 5.3: semantic similarity ───────────────────────────────────────────

# Cosine similarity between short ISO text and long impl docs typically ranges 0.1–0.55.
# Thresholds are calibrated to this range (not the 0–1 absolute scale).
_SEMANTIC_PASS_THRESHOLD = Decimal("0.42")
_SEMANTIC_WARN_THRESHOLD = Decimal("0.28")

_CLAUDE_PASS_THRESHOLD = Decimal("0.70")
_CLAUDE_WARN_THRESHOLD = Decimal("0.45")

# Lazy-loaded sentence-transformers model (downloaded ~80MB on first use)
_SEMANTIC_MODEL = None


def _get_semantic_model():
    global _SEMANTIC_MODEL
    if _SEMANTIC_MODEL is None:
        from sentence_transformers import SentenceTransformer  # type: ignore
        logger.info("Loading sentence-transformers model all-MiniLM-L6-v2 …")
        _SEMANTIC_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
        logger.info("Sentence-transformers model loaded")
    return _SEMANTIC_MODEL


def _build_iso_text(db: DBSession, framework, group: ControlGroup) -> str:
    """Build ISO control text for a group (title + description of linked controls)."""
    control_ids: list[str] = group.stacked_control_ids or []
    if framework and control_ids:
        fw_controls = db.execute(
            select(FrameworkControl).where(
                FrameworkControl.framework_id == framework.id,
                FrameworkControl.control_id.in_(control_ids),
            )
        ).scalars().all()
        parts = [f"{fc.title} {fc.description or ''}" for fc in fw_controls]
        text = " ".join(parts).strip()
        if text:
            return text
    return group.name


def _semantic_status(strength: Decimal, pass_t: Decimal, warn_t: Decimal) -> QAStatus:
    if strength >= pass_t:
        return QAStatus.PASS
    if strength >= warn_t:
        return QAStatus.WARNING
    return QAStatus.FAIL


def run_semantic_mini_check(
    db: DBSession,
    group_id: uuid.UUID | None = None,
) -> dict:
    """Run semantic similarity check using sentence-transformers all-MiniLM-L6-v2.

    Encodes ISO control text and UG/TG implementation content as vectors, then
    computes cosine similarity. No API key required — runs entirely on CPU.

    Deletes previous SEMANTIC results before writing fresh ones.
    """
    t0 = time.monotonic()
    run_date = datetime.now(timezone.utc)

    os_client = search_service.get_client()
    os_available = os_client is not None
    if not os_available:
        logger.warning("OpenSearch unavailable — semantic mini check will mark all as needs_review")

    try:
        from sentence_transformers import util as st_util  # type: ignore
        model = _get_semantic_model()
    except ImportError:
        raise RuntimeError(
            "sentence-transformers not installed. "
            "Add it to requirements.txt and rebuild the container."
        )

    q = select(ControlGroup).order_by(ControlGroup.group_code)
    if group_id:
        q = q.where(ControlGroup.id == group_id)
    groups = db.execute(q).scalars().all()

    _framework_codes = {
        ProductFamily.ISMS: "ISO27001_2022",
        ProductFamily.PRIVACY: "ISO27701",
        ProductFamily.CLOUD: "ISO27018",
    }
    frameworks = {
        family: db.execute(
            select(Framework).where(Framework.code == code)
        ).scalar_one_or_none()
        for family, code in _framework_codes.items()
    }

    del_q = delete(CorrelationResult).where(
        CorrelationResult.correlation_method == CorrelationMethod.SEMANTIC
    )
    if group_id:
        del_q = del_q.where(CorrelationResult.control_group_id == group_id)
    db.execute(del_q)

    stats: dict[str, int] = {"total": 0, "pass": 0, "warning": 0, "fail": 0, "needs_review": 0}

    for group in groups:
        doc_id = f"{group.group_code}:sem"
        framework = frameworks.get(group.product_family)
        product_label = group.product_family.value.lower() if group.product_family else "isms"
        iso_text = _build_iso_text(db, framework, group)
        impl_text = _fetch_group_full_text(os_client, group.group_code, language="en")[:2000] if os_available else ""

        if not impl_text:
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=doc_id,
                correlation_method=CorrelationMethod.SEMANTIC,
                correlation_strength=Decimal("0"),
                qa_status=QAStatus.NEEDS_REVIEW,
                coverage_keywords=[],
                missing_keywords=[],
                run_date=run_date,
                metadata_={
                    "product_type": product_label,
                    "reason": "no_implementation_content",
                    "model": "all-MiniLM-L6-v2",
                },
            ))
            stats["total"] += 1
            stats["needs_review"] += 1
            continue

        embeddings = model.encode([iso_text, impl_text], convert_to_tensor=True)
        cosine = float(st_util.cos_sim(embeddings[0], embeddings[1]))
        # Clamp to [0, 1] — cosine can be negative for unrelated texts
        cosine = max(0.0, min(1.0, cosine))
        strength = Decimal(str(round(cosine, 4)))
        status = _semantic_status(strength, _SEMANTIC_PASS_THRESHOLD, _SEMANTIC_WARN_THRESHOLD)

        iso_word_count = len(iso_text.split())
        db.add(CorrelationResult(
            control_group_id=group.id,
            document_id=doc_id,
            correlation_method=CorrelationMethod.SEMANTIC,
            correlation_strength=strength,
            qa_status=status,
            coverage_keywords=[],
            missing_keywords=[],
            run_date=run_date,
            metadata_={
                "product_type": product_label,
                "model": "all-MiniLM-L6-v2",
                "iso_text": iso_text[:400],
                "iso_word_count": iso_word_count,
                "short_iso_text": iso_word_count < 15,
                "impl_text_chars": len(impl_text),
            },
        ))
        stats["total"] += 1
        stats[status.value] += 1

    db.commit()
    stats["duration_ms"] = int((time.monotonic() - t0) * 1000)
    logger.info("Semantic mini check complete: %s", stats)
    return stats


def run_semantic_claude_check(
    db: DBSession,
    group_id: uuid.UUID | None = None,
) -> dict:
    """Run semantic analysis using Anthropic Claude API.

    Sends ISO control requirements + implementation text to Claude, asks for a
    structured JSON score (0–100) with reasoning and gap list.

    Requires ANTHROPIC_API_KEY to be configured in settings.
    Deletes previous SEMANTIC_CLAUDE results before writing fresh ones.
    """
    import json as _json

    from src.core.config import get_settings
    settings = get_settings()

    if not settings.anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY not configured — add it to .env to use Claude semantic QA.")

    import anthropic as _anthropic
    client = _anthropic.Anthropic(api_key=settings.anthropic_api_key)

    t0 = time.monotonic()
    run_date = datetime.now(timezone.utc)

    os_client = search_service.get_client()
    os_available = os_client is not None

    q = select(ControlGroup).order_by(ControlGroup.group_code)
    if group_id:
        q = q.where(ControlGroup.id == group_id)
    groups = db.execute(q).scalars().all()

    _framework_codes = {
        ProductFamily.ISMS: "ISO27001_2022",
        ProductFamily.PRIVACY: "ISO27701",
        ProductFamily.CLOUD: "ISO27018",
    }
    frameworks = {
        family: db.execute(
            select(Framework).where(Framework.code == code)
        ).scalar_one_or_none()
        for family, code in _framework_codes.items()
    }
    _standard_names = {
        ProductFamily.ISMS: "ISO 27001:2022",
        ProductFamily.PRIVACY: "ISO 27701:2025",
        ProductFamily.CLOUD: "ISO 27018:2025",
    }

    del_q = delete(CorrelationResult).where(
        CorrelationResult.correlation_method == CorrelationMethod.SEMANTIC_CLAUDE
    )
    if group_id:
        del_q = del_q.where(CorrelationResult.control_group_id == group_id)
    db.execute(del_q)

    stats: dict[str, int] = {"total": 0, "pass": 0, "warning": 0, "fail": 0, "needs_review": 0}

    _PROMPT_TEMPLATE = """\
You are a {standard_name} QA auditor. Rate how well the implementation \
documentation addresses the ISO control requirements below.

ISO CONTROL REQUIREMENTS:
{iso_text}

IMPLEMENTATION DOCUMENTATION (excerpt):
{impl_text}

Respond with a JSON object ONLY — no other text:
{{"score": <integer 0-100>, "reasoning": "<2-3 sentence explanation>", "gaps": ["<gap 1>", "<gap 2>"]}}

score guide: 0=no coverage, 30=minimal, 50=partial, 70=good, 85=strong, 100=comprehensive.
gaps: list up to 3 specific missing topics; empty list [] if score>=85."""

    for group in groups:
        doc_id = f"{group.group_code}:sem_claude"
        framework = frameworks.get(group.product_family)
        product_label = group.product_family.value.lower() if group.product_family else "isms"
        standard_name = _standard_names.get(group.product_family, "ISO 27001:2022")
        iso_text = _build_iso_text(db, framework, group)
        impl_text = _fetch_group_full_text(os_client, group.group_code, language="en")[:3000] if os_available else ""

        if not impl_text:
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=doc_id,
                correlation_method=CorrelationMethod.SEMANTIC_CLAUDE,
                correlation_strength=Decimal("0"),
                qa_status=QAStatus.NEEDS_REVIEW,
                coverage_keywords=[],
                missing_keywords=[],
                run_date=run_date,
                metadata_={
                    "product_type": product_label,
                    "reason": "no_implementation_content",
                    "model": settings.ai_model,
                },
            ))
            stats["total"] += 1
            stats["needs_review"] += 1
            continue

        prompt = _PROMPT_TEMPLATE.format(
            standard_name=standard_name,
            iso_text=iso_text[:600],
            impl_text=impl_text,
        )

        score_raw = 0
        reasoning = ""
        gaps: list[str] = []
        try:
            response = client.messages.create(
                model=settings.ai_model,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            # Strip markdown code fences if present
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            parsed = _json.loads(text)
            score_raw = max(0, min(100, int(parsed.get("score", 0))))
            reasoning = str(parsed.get("reasoning", ""))
            gaps = [str(g) for g in parsed.get("gaps", [])][:3]
        except (_anthropic.RateLimitError, _anthropic.APIStatusError) as e:
            logger.warning("Claude API error for group %s: %s", group.group_code, e)
            db.add(CorrelationResult(
                control_group_id=group.id,
                document_id=doc_id,
                correlation_method=CorrelationMethod.SEMANTIC_CLAUDE,
                correlation_strength=Decimal("0"),
                qa_status=QAStatus.NEEDS_REVIEW,
                coverage_keywords=[],
                missing_keywords=[],
                run_date=run_date,
                metadata_={"product_type": product_label, "reason": f"api_error: {e}", "model": settings.ai_model},
            ))
            stats["total"] += 1
            stats["needs_review"] += 1
            time.sleep(1)
            continue
        except Exception as e:
            logger.warning("Claude response parse error for group %s: %s", group.group_code, e)
            score_raw = 0
            reasoning = f"Parse error: {e}"
            gaps = []

        strength = Decimal(str(score_raw)) / Decimal("100")
        status = _semantic_status(strength, _CLAUDE_PASS_THRESHOLD, _CLAUDE_WARN_THRESHOLD)

        db.add(CorrelationResult(
            control_group_id=group.id,
            document_id=doc_id,
            correlation_method=CorrelationMethod.SEMANTIC_CLAUDE,
            correlation_strength=strength,
            qa_status=status,
            coverage_keywords=[],
            missing_keywords=gaps,
            run_date=run_date,
            metadata_={
                "product_type": product_label,
                "score": score_raw,
                "reasoning": reasoning,
                "gaps": gaps,
                "model": settings.ai_model,
            },
        ))
        stats["total"] += 1
        stats[status.value] += 1

        # Brief pause to stay within API rate limits
        time.sleep(0.3)

    db.commit()
    stats["duration_ms"] = int((time.monotonic() - t0) * 1000)
    logger.info("Semantic Claude check complete: %s", stats)
    return stats
