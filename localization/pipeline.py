#!/usr/bin/env python3
"""Localization pipeline for the ISMS CORE Chinese content packs.

Two output tracks, one source of truth:

    English source  --translate-->  Traditional (zh-TW)  --derive-->  Simplified (zh-CN)

Deriving the Simplified tree from the Traditional one keeps the two variants
from drifting apart. Deriving is not a plain character conversion, though.
OpenCC converts glyphs but does not know Taiwan IT vocabulary, so its plain
t2s output is wrong for exactly the words this corpus is made of::

    資訊安全 -> 资讯安全   (want 信息安全)
    網路     -> 网路       (want 网络)
    軟體     -> 软体       (want 软件)
    稽核     -> 稽核       (want 审计)
    矯正措施 -> 矫正措施   (want 纠正措施)
    風險評鑑 -> 风险评鉴   (want 风险评估)

So the termbase pass runs FIRST, on the Traditional text, and OpenCC only
mops up what is left. The order matters and is not interchangeable: OpenCC
rewrites 網路 to 网路, after which the termbase key 網路 no longer matches.
tests/test_pipeline.py pins that order.

Commands:
    python3 localization/pipeline.py plan [--pack PACK ...] [--lang zh-TW]
    python3 localization/pipeline.py derive <hant.md> [--out hans.md]
    python3 localization/pipeline.py audit [--pack PACK ...]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LOCALIZATION = REPO / "localization"
TERMBASE_PATH = LOCALIZATION / "glossary" / "zh-termbase.json"

PACKS = ["isms-core-framework", "isms-core-operational", "isms-core-privacy",
         "isms-core-cloud", "isms-core-ai", "isms-core-ext", "isms-core-sec"]
DOC_TYPE_DIRS = {"POL", "IMP", "SCR", "REF", "CTX", "FORM", "WKBK", "INS"}
SKIP_LANG_DIR = re.compile(r"/(de|fr|it|tr|zh-TW|zh-CN)/")

LANG_PAIR = {"zh-TW": "zh-CN", "zh-CN": "zh-TW"}


def lang_suffix(lang: str) -> str:
    """zh-TW -> ZH-TW, the form used in watermarks and file names."""
    return lang.upper()


def load_termbase(path: Path = TERMBASE_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _opencc():
    try:
        import opencc
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit(
            "opencc is required for Simplified derivation: pip install opencc"
        ) from exc
    return opencc.OpenCC("t2s")


def _term_pattern(termbase: dict, from_col: str) -> re.Pattern | None:
    """Alternation of every source-side term, longest first.

    A single pass, so a shorter term can never rewrite part of a longer one
    that has not been matched yet (資訊 must not eat into 資訊安全).
    """
    terms = [e[from_col] for e in termbase["entries"] if e.get(from_col)]
    terms = [t for t in terms if t and "\n" not in t]
    if not terms:
        return None
    terms.sort(key=len, reverse=True)
    return re.compile("|".join(re.escape(t) for t in terms))


def to_hans(hant_text: str, termbase: dict, cc=None) -> str:
    """Traditional -> Simplified: termbase first, OpenCC for the residue."""
    lookup = {e["hant"]: e["hans"]
              for e in termbase["entries"]
              if e.get("hant") and e.get("hans") and "\n" not in e["hant"]}
    pattern = _term_pattern(termbase, "hant")
    text = pattern.sub(lambda m: lookup[m.group(0)], hant_text) if pattern else hant_text
    cc = cc if cc is not None else _opencc()
    return cc.convert(text)


def flip_watermark(text: str, from_lang: str, to_lang: str) -> str:
    """Rewrite the ISO language suffix inside the ISMS-CORE watermark."""
    return re.sub(
        rf"<!--\s*ISMS-CORE:([A-Z]+):([A-Za-z0-9.\-]+?)-{re.escape(lang_suffix(from_lang))}:",
        lambda m: f"<!-- ISMS-CORE:{m.group(1)}:{m.group(2)}-{lang_suffix(to_lang)}:",
        text,
        count=1,
    )


def derive_simplified(hant_path: Path, out_path: Path | None = None,
                      termbase: dict | None = None) -> Path:
    """Write the Simplified sibling of a Traditional file."""
    termbase = termbase or load_termbase()
    from_lang, to_lang = "zh-TW", "zh-CN"
    text = hant_path.read_text(encoding="utf-8")

    derived = flip_watermark(text, from_lang, to_lang)
    derived = to_hans(derived, termbase)

    # Derivation must never change the line count: the two variants have to
    # stay structurally identical or the alignment invariant is meaningless.
    src_lines, dst_lines = text.count("\n") + 1, derived.count("\n") + 1
    if src_lines != dst_lines:
        raise ValueError(
            f"derivation changed line count: {src_lines} -> {dst_lines}"
        )

    if out_path is None:
        name = hant_path.name.replace(f" - {lang_suffix(from_lang)}.md",
                                      f" - {lang_suffix(to_lang)}.md")
        # Language directories are siblings under the document-type directory
        # (POL/de, POL/fr, POL/zh-CN), so the target is hant's grandparent —
        # not hant.parent, which would nest zh-CN inside zh-TW.
        out_path = hant_path.parent.parent / to_lang / name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(derived, encoding="utf-8")
    return out_path


def _source_docs(packs: list[str]) -> list[Path]:
    out: list[Path] = []
    for pack in packs:
        root = REPO / pack
        if not root.is_dir():
            continue
        for path in root.rglob("*.md"):
            if SKIP_LANG_DIR.search(str(path)):
                continue
            if path.parent.name in DOC_TYPE_DIRS:
                out.append(path)
    return sorted(out)


def docid(path: Path) -> str:
    """The document ID, which is the part before the first ' - ' of the stem.

    Translation files cannot be matched by file name: the title is translated,
    so 'ISMS-OP-POL-A.8.9 - Configuration Management.md' is paired with
    'ISMS-OP-POL-A.8.9 - Konfigurationsmanagement - DE.md'. The document ID is
    the only stable join key.
    """
    return path.stem.split(" - ")[0]


def target_path(en_path: Path, lang: str, title: str) -> Path:
    """<doctype>/<lang>/<DOCID> - <Translated Title> - <LANG>.md"""
    return en_path.parent / lang / f"{docid(en_path)} - {title} - {lang_suffix(lang)}.md"


def is_translated(en_path: Path, lang: str) -> bool:
    lang_dir = en_path.parent / lang
    if not lang_dir.is_dir():
        return False
    want = docid(en_path)
    return any(docid(p) == want for p in lang_dir.glob("*.md"))


def plan(packs: list[str], lang: str) -> list[Path]:
    """Source documents that have no translation yet in the given language."""
    return [en for en in _source_docs(packs) if not is_translated(en, lang)]


def audit(packs: list[str]) -> dict:
    """Coverage per language, plus source documents translated nowhere."""
    docs = _source_docs(packs)
    langs = ["de", "fr", "it", "zh-TW", "zh-CN"]
    report = {"english_documents": len(docs), "languages": {}, "untranslated": []}
    for lang in langs:
        report["languages"][lang] = sum(1 for en in docs if is_translated(en, lang))
    for en in docs:
        if not any(is_translated(en, lang) for lang in langs):
            report["untranslated"].append(str(en.relative_to(REPO)))
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="source documents still untranslated")
    p_plan.add_argument("--pack", action="append", default=[])
    p_plan.add_argument("--lang", default="zh-TW")

    p_derive = sub.add_parser("derive", help="Traditional file -> Simplified file")
    p_derive.add_argument("hant", type=Path)
    p_derive.add_argument("--out", type=Path, default=None)

    p_audit = sub.add_parser("audit", help="translation coverage across packs")
    p_audit.add_argument("--pack", action="append", default=[])

    args = ap.parse_args(argv)
    # Only plan and audit take --pack; derive names its file directly.
    packs = getattr(args, "pack", None) or PACKS

    if args.cmd == "plan":
        pending = plan(packs, args.lang)
        for path in pending:
            print(path.relative_to(REPO))
        print(f"\n{len(pending)} document(s) pending for {args.lang}")
        return 0

    if args.cmd == "derive":
        out = derive_simplified(args.hant, args.out)
        print(f"wrote {out}")
        return 0

    if args.cmd == "audit":
        report = audit(packs)
        print(f"English documents: {report['english_documents']}\n")
        for lang, n in report["languages"].items():
            print(f"  {lang:6s} {n:4d}")
        print(f"\nTranslated in no language: {len(report['untranslated'])}")
        for path in report["untranslated"][:10]:
            print(f"  {path}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
