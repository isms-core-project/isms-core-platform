"""ISMS Compass — gap analysis service.

Retrieves ISMS CORE Gold Standard reference content from OpenSearch (BM25),
then calls Claude to produce a structured gap analysis report comparing
the submitted document against the Gold Standard for a given control group.
"""

import json
import logging
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.domain.control_groups import ControlGroup
from src.services import search_service

logger = logging.getLogger(__name__)

DISCLAIMER = (
    "This analysis is based on ISO 27001:2022 requirements and ISMS CORE reference content. "
    "It is provided for guidance only and does not guarantee audit compliance. "
    "Independent review by a qualified ISMS practitioner is recommended before relying on this output."
)

_ANALYSIS_PROMPT = """You are an ISO 27001:2022 expert performing a gap analysis on a submitted document against the ISMS CORE Gold Standard for {control_name} ({control_code}).

## ISMS CORE Gold Standard Reference
The following is extracted from ISMS CORE's certified reference documentation for this control group:

{reference_content}

## Submitted Document
{submitted_content}

## Task
Analyse the submitted document against the Gold Standard reference above. Return ONLY valid JSON — no prose, no markdown fences — matching this exact schema:

{{
  "coverage_score": <integer 0-100>,
  "summary": "<2-3 sentence executive summary of the document's overall coverage>",
  "strengths": [
    {{"topic": "<topic name>", "detail": "<why this is well covered>"}}
  ],
  "gaps": [
    {{
      "topic": "<missing or inadequate topic>",
      "severity": "<high|medium|low>",
      "description": "<what is missing or inadequate, with reference to Gold Standard>",
      "iso_clause": "<most relevant ISO 27001:2022 clause, e.g. A.5.1>",
      "recommendation": "<specific, actionable recommendation>"
    }}
  ]
}}

Scoring guide:
- 90–100: All key requirements addressed with appropriate detail
- 70–89: Most requirements covered, minor gaps
- 50–69: Core topics present but significant gaps
- 30–49: Partial coverage, major gaps
- 0–29: Minimal relevant content

Be specific and actionable. Reference the Gold Standard directly. Use British English spelling."""


def _fetch_reference_content(group_code: str, max_chars: int = 8000) -> str:
    """Retrieve Gold Standard reference content from OpenSearch for a control group."""
    from src.services.search_service import IDX_IMPLEMENTATIONS, IDX_POLICIES

    client = search_service.get_client()
    if not client:
        logger.warning("Compass: OpenSearch unavailable — analysis without reference content.")
        return f"[OpenSearch unavailable — analysis based on ISO 27001:2022 knowledge for {group_code.upper()} only.]"

    parts: list[str] = []
    code = group_code.lower()

    for index, label in [(IDX_POLICIES, "POLICY"), (IDX_IMPLEMENTATIONS, "IMP")]:
        try:
            resp = client.search(
                index=index,
                body={
                    "query": {"term": {"control_group_code": code}},
                    "size": 6,
                    "_source": ["document_id", "title", "sections"],
                },
            )
            for hit in resp["hits"]["hits"]:
                src = hit["_source"]
                parts.append(f"[{label}: {src.get('document_id', '')} — {src.get('title', '')}]")
                for section in (src.get("sections") or [])[:3]:
                    heading = section.get("heading", "")
                    body = (section.get("body") or "")[:400]
                    if heading:
                        parts.append(f"### {heading}")
                    if body:
                        parts.append(body)
                parts.append("")
        except Exception as e:
            logger.warning("Compass: %s search error: %s", index, e)

    reference = "\n".join(parts)[:max_chars]
    if not reference.strip():
        reference = f"[No ISMS CORE reference content indexed for {group_code.upper()}. Analysis based on ISO 27001:2022 requirements only.]"
    return reference


def _get_effective_model(db: DBSession) -> str:
    """Return AI model from org settings, falling back to config default."""
    from src.domain.organisations import Organisation
    settings = get_settings()
    org = db.execute(select(Organisation)).scalar_one_or_none()
    if org and org.settings and org.settings.get("ai_model"):
        return org.settings["ai_model"]
    return settings.ai_model


def analyse_document(db: DBSession, group_code: str, document_text: str) -> dict[str, Any]:
    """Run ISMS Compass gap analysis on a document against the Gold Standard."""
    settings = get_settings()
    if not settings.anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY not configured. Add it to platform/.env.")

    model = _get_effective_model(db)

    # Resolve control group name
    cg = db.execute(
        select(ControlGroup).where(ControlGroup.group_code == group_code.lower())
    ).scalar_one_or_none()
    control_name = cg.name if cg else group_code.upper()

    reference_content = _fetch_reference_content(group_code)

    # Truncate submitted doc to leave room in context window
    submitted = document_text[:6000]
    if len(document_text) > 6000:
        submitted += f"\n\n[Document truncated — {len(document_text):,} chars total, showing first 6,000]"

    prompt = _ANALYSIS_PROMPT.format(
        control_name=control_name,
        control_code=group_code.upper(),
        reference_content=reference_content,
        submitted_content=submitted,
    )

    import anthropic

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    raw_text = ""
    tokens_used = 0

    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = response.content[0].text.strip()
        tokens_used = response.usage.input_tokens + response.usage.output_tokens

        # Strip markdown code fences if model wraps in ```json ... ```
        if raw_text.startswith("```"):
            lines = raw_text.split("\n")
            raw_text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

        result = json.loads(raw_text)

    except json.JSONDecodeError as e:
        logger.error("Compass: JSON parse failed. Raw: %.200s", raw_text)
        raise ValueError(f"AI returned malformed response: {e}")
    except anthropic.AuthenticationError:
        raise ValueError("Invalid Anthropic API key.")
    except anthropic.RateLimitError:
        raise ValueError("Rate limit reached — please try again shortly.")
    except Exception as e:
        logger.error("Compass: Claude API error: %s", e)
        raise ValueError(f"AI error: {e}")

    return {
        "control_group_code": group_code.lower(),
        "control_group_name": control_name,
        "coverage_score": int(result.get("coverage_score", 0)),
        "summary": result.get("summary", ""),
        "strengths": result.get("strengths", []),
        "gaps": result.get("gaps", []),
        "disclaimer": DISCLAIMER,
        "model_used": model,
        "tokens_used": tokens_used,
    }
