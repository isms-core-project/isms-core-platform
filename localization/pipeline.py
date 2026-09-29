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
    python3 localization/pipeline.py derive-doc <README.zh-TW.md> [--out OUT]
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

sys.path.insert(0, str(LOCALIZATION / "glossary"))
from charsets import LANGUAGE_LINE_RE  # noqa: E402

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


def derivable(termbase: dict) -> list[dict]:
    """Termbase entries the substitution pass is allowed to apply.

    Single-character hant keys are held back, and that is the whole reason this
    function exists. Substitution is an alternation over raw text with no word
    segmentation — Chinese does not have word boundaries to anchor on — so a
    one-character key fires inside every word that happens to contain the
    character. 得 -> 可 turned 取得 (to obtain) into 取可 in the shipped
    CLD-SEC-POL-A.5.38, and 欄 -> 列 fired inside 欄位 (saved only because the
    longer entry 欄位 -> 字段 matched first).

    Neither entry is *wrong*. 得 really is the Traditional modal "may" and 欄
    really is "column"; they belong in the glossary for whoever translates the
    next document. What a one-character key cannot do is express a word-level
    decision, so they stay in the termbase and out of derivation.

    Nothing is lost by holding them back: every one-character entry is
    glyph-neutral or a glyph pair OpenCC already handles (得 converts to
    itself, 應 -> 应, 欄 -> 栏), so the residue pass produces the right
    characters either way.
    """
    return [e for e in termbase["entries"]
            if e.get("hant") and e.get("hans") and "\n" not in e["hant"]
            and len(e["hant"]) > 1]


def _term_pattern(termbase: dict) -> re.Pattern | None:
    """Alternation of every derivable term, longest first.

    A single pass, so a shorter term can never rewrite part of a longer one
    that has not been matched yet (資訊 must not eat into 資訊安全).
    """
    terms = sorted({e["hant"] for e in derivable(termbase)}, key=len, reverse=True)
    if not terms:
        return None
    return re.compile("|".join(re.escape(t) for t in terms))


def to_hans(hant_text: str, termbase: dict, cc=None) -> str:
    """Traditional -> Simplified: termbase first, OpenCC for the residue."""
    lookup = {e["hant"]: e["hans"] for e in derivable(termbase)}
    pattern = _term_pattern(termbase)
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


# --- Repository documents ---------------------------------------------------
# README.md and the other top-level documents are localized in place, as
# <base>.zh-TW.md / <base>.zh-CN.md, rather than under a language directory.
# Each copy opens with one line naming the three variants. The names are
# written in their own script — 繁體中文, 简体中文 — and are deliberately not
# translated: a reader looks for their own label in their own characters. So
# the deriver may not convert that line, or one pass of t2s would leave the
# Simplified copy advertising 繁体中文.

LANGUAGE_NAMES = {"en": "English", "zh-TW": "繁體中文", "zh-CN": "简体中文"}
SWITCHER_LANGS = ("en", "zh-TW", "zh-CN")

# Matches the language line in any of its three spellings. Only that one line
# carries both labels, so the test does not need to be anchored on markup.
#
# The pattern lives in charsets because the script gate has to recognise this
# same line and exempt it — it is the one place both scripts legitimately
# appear in a single file. Two copies of a subtle pattern drift, and the
# failure mode is silent: the gate would just start rejecting every localized
# README it had previously accepted.
SWITCHER_RE = LANGUAGE_LINE_RE

# The line is lifted out before conversion and put back afterwards. It has to
# survive as a single ASCII line, so the placeholder is an HTML comment the
# termbase cannot match; converting first and repairing afterwards would mean
# writing a second pattern for the damaged spelling.
SWITCHER_PLACEHOLDER = "<!--ISMS-CORE:LANG-SWITCHER-->"

DOC_LANG_RE = re.compile(r"^(?P<base>.+)\.(?P<lang>zh-TW|zh-CN)\.md$")


def switcher(base: str, lang: str) -> str:
    """The language line for <base>.md seen from <lang>, in one canonical form."""
    parts = []
    for other in SWITCHER_LANGS:
        name = LANGUAGE_NAMES[other]
        if other == lang:
            parts.append(f"<strong>{name}</strong>")
        else:
            href = f"{base}.md" if other == "en" else f"{base}.{other}.md"
            parts.append(f'<a href="{href}">{name}</a>')
    return f'<p align="center">{" · ".join(parts)}</p>'


def derive_doc(hant_path: Path, out_path: Path | None = None,
               termbase: dict | None = None) -> Path:
    """Write the Simplified sibling of a repository document.

    Same contract as derive_simplified — termbase first, OpenCC for the
    residue, line count unchanged — but the pair sits side by side as
    <base>.zh-TW.md / <base>.zh-CN.md and the language line is restored
    verbatim instead of converted.
    """
    m = DOC_LANG_RE.match(hant_path.name)
    if not m or m.group("lang") != "zh-TW":
        raise ValueError(f"not a zh-TW repository document: {hant_path.name}")
    if out_path is None:
        out_path = hant_path.with_name(f"{m.group('base')}.zh-CN.md")
    termbase = termbase or load_termbase()

    text = hant_path.read_text(encoding="utf-8")
    protected = SWITCHER_RE.sub(SWITCHER_PLACEHOLDER, text, count=1)
    if SWITCHER_PLACEHOLDER not in protected:
        raise ValueError(
            f"{hant_path.name} has no language line; every localized repository "
            f"document opens with one (see switcher())"
        )

    derived = to_hans(protected, termbase)

    # Cross-links between repository documents name the Chinese sibling by its
    # language tag, and that tag means "mine": from the Traditional README,
    # PARADIGM.zh-TW.md is the Traditional PARADIGM. In the derived file the
    # same sentence has to reach PARADIGM.zh-CN.md, or every cross-link lands
    # on the other script. Rewriting the tag moves link targets and link text
    # together, which is why they are written the same way.
    #
    # Done before the switcher is restored, so the switcher's link to the
    # *other* variant — the one link that must keep the zh-TW tag — is not
    # caught up in it.
    derived = derived.replace(".zh-TW.md", ".zh-CN.md")

    derived = derived.replace(SWITCHER_PLACEHOLDER, switcher(m.group("base"), "zh-CN"))

    src_lines, dst_lines = text.count("\n") + 1, derived.count("\n") + 1
    if src_lines != dst_lines:
        raise ValueError(
            f"derivation changed line count: {src_lines} -> {dst_lines}"
        )

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

    p_doc = sub.add_parser("derive-doc",
                           help="README.zh-TW.md -> README.zh-CN.md")
    p_doc.add_argument("hant", type=Path)
    p_doc.add_argument("--out", type=Path, default=None)

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

    if args.cmd == "derive-doc":
        out = derive_doc(args.hant, args.out)
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
