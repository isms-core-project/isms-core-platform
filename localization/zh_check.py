#!/usr/bin/env python3
"""Structural and quality gate for ISMS CORE Chinese localizations.

A translated document must be a line-aligned rendering of its English source:
the existing de/fr/it trees hold this to within one line on 98% of pairs
(measured: 47/53 identical, 52/53 within +/-1, on isms-core-operational).

This module exists because a previous localization attempt (upstream PR #2)
was closed for shipping filler: 1240 files of exactly 33 lines, each a generic
three-paragraph template with the English title left untranslated, plus four
real documents deleted in passing. Those failure modes are encoded here as
checks, and as tests in tests/test_zh_check.py.

Usage:
    python3 localization/zh_check.py <source_en.md> <translated.md> [--lang zh-Hant]

Exit code is 0 when every gate passes, 1 when any gate fails.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "glossary"))
from charsets import leaks  # noqa: E402

# Structural markers whose counts must match the source exactly.
#
# Headings are counted at every level, not just ## and ###: the cloud policy
# documents put their major sections at level 1, so a check limited to h2/h3
# would silently skip the entire heading structure of those files.
HEADING_RE = re.compile(r"^(#{1,6}) ")
TABLE_ROW_RE = re.compile(r"^\|")
FENCE_RE = re.compile(r"^```")
CHECKBOX_RE = re.compile(r"^\s*[-*] \[[ xX]\]")

# Watermark: <!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-DE:operational:OP-POL:a.8.9 -->
WATERMARK_RE = re.compile(r"<!--\s*ISMS-CORE:[A-Z]+:([A-Za-z0-9.\-]+):")
QA_FOOTER_RE = re.compile(r"<!--\s*QA_VERIFIED:\s*\d{4}-\d{2}-\d{2}\s*-->")

# A translated body should contain at least this share of CJK characters.
MIN_CJK_RATIO = 0.10
# Below this many lines, a translation of a substantial document is a stub.
STUB_LINE_THRESHOLD = 40
STUB_SOURCE_LINES = 100
# Tolerance on total line count versus the English source.
MAX_LINE_DELTA = 1


@dataclass
class Finding:
    gate: str
    detail: str
    severity: str = "fail"  # "fail" | "warn"

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.gate}: {self.detail}"


def _heading_counts(text: str) -> dict[int, int]:
    counts: dict[int, int] = {}
    for ln in text.splitlines():
        m = HEADING_RE.match(ln)
        if m:
            counts[len(m.group(1))] = counts.get(len(m.group(1)), 0) + 1
    return counts


def _counts(text: str) -> dict[str, int]:
    lines = text.splitlines()
    return {
        "lines": len(lines),
        "table_rows": sum(1 for ln in lines if TABLE_ROW_RE.match(ln)),
        "fences": sum(1 for ln in lines if FENCE_RE.match(ln)),
        "checkboxes": sum(1 for ln in lines if CHECKBOX_RE.match(ln)),
    }


def _first_title(text: str) -> str | None:
    """Return the bolded title line, e.g. '**ISMS-OP-POL-A.8.9 - Foo**'."""
    for line in text.splitlines():
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def _cjk_ratio(text: str) -> float:
    body = re.sub(r"[#*|\-`>\s]+", "", text)
    if not body:
        return 0.0
    cjk = sum(1 for ch in body if "㐀" <= ch <= "鿿")
    return cjk / len(body)


def check(source_text: str, translated_text: str, lang: str) -> list[Finding]:
    """Return every gate result for one source/translation pair."""
    findings: list[Finding] = []
    src, dst = _counts(source_text), _counts(translated_text)

    # --- Gate 1: structure preserved (the alignment guarantee) -------------
    src_h, dst_h = _heading_counts(source_text), _heading_counts(translated_text)
    for level in sorted(set(src_h) | set(dst_h)):
        if src_h.get(level, 0) != dst_h.get(level, 0):
            findings.append(Finding(
                "structure",
                f"h{level} headings: source {src_h.get(level, 0)} "
                f"vs translation {dst_h.get(level, 0)}",
            ))

    for key, label in (("table_rows", "table rows"), ("fences", "code fences"),
                       ("checkboxes", "checkboxes")):
        if src[key] != dst[key]:
            findings.append(Finding(
                "structure",
                f"{label}: source {src[key]} vs translation {dst[key]}",
            ))

    if abs(dst["lines"] - src["lines"]) > MAX_LINE_DELTA:
        findings.append(Finding(
            "structure",
            f"line count: source {src['lines']} vs translation {dst['lines']} "
            f"(tolerance +/-{MAX_LINE_DELTA})",
        ))

    # --- Gate 2: not filler (the PR #2 failure mode) ----------------------
    if src["lines"] >= STUB_SOURCE_LINES and dst["lines"] <= STUB_LINE_THRESHOLD:
        findings.append(Finding(
            "substance",
            f"stub: {dst['lines']} lines translating a {src['lines']}-line document",
        ))

    ratio = _cjk_ratio(translated_text)
    if ratio < MIN_CJK_RATIO:
        findings.append(Finding(
            "substance",
            f"CJK ratio {ratio:.3f} below {MIN_CJK_RATIO} — body may be untranslated",
        ))

    # The source title is '**<DOCID> - <English title>**'. A translation that
    # keeps the English title verbatim is the tell that nothing was translated.
    src_title, dst_title = _first_title(source_text), _first_title(translated_text)
    if src_title and dst_title:
        src_words = re.sub(r"^[\w.\-]+ [-—] ", "", src_title)
        if src_words and src_words in dst_title:
            findings.append(Finding(
                "substance",
                f"title left in English: {dst_title!r} still contains {src_words!r}",
            ))

    # --- Gate 3: identifiers ---------------------------------------------
    src_wm = WATERMARK_RE.search(source_text)
    dst_wm = WATERMARK_RE.search(translated_text)
    if not dst_wm:
        findings.append(Finding("identifier", "watermark comment missing"))
    elif src_wm:
        want = f"{src_wm.group(1)}-{lang.upper()}"
        if dst_wm.group(1) != want:
            findings.append(Finding(
                "identifier",
                f"watermark id {dst_wm.group(1)!r}, expected {want!r}",
            ))

    # --- Gate 4: QA marker required for promotion -------------------------
    if not QA_FOOTER_RE.search(translated_text):
        findings.append(Finding(
            "promotion",
            "missing '<!-- QA_VERIFIED: YYYY-MM-DD -->' footer",
        ))

    # --- Gate 5: one script, not two --------------------------------------
    # A hand-written translation picks up stray characters from the other
    # script: 发现 typed into a Traditional file, or 記錄 into a Simplified one.
    # It reads as normal Chinese and survives every other gate, so it needs its
    # own check. Reported per character with line numbers, because a bare list
    # of glyphs is not actionable in a 150-line document.
    for ch, lines in sorted(leaks(translated_text, lang).items()):
        shown = ", ".join(str(n) for n in lines[:8])
        more = f" (+{len(lines) - 8} more)" if len(lines) > 8 else ""
        findings.append(Finding(
            "script",
            f"{ch!r} is not a {lang} character — lines {shown}{more}",
        ))

    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("source", type=Path, help="English source markdown")
    ap.add_argument("translated", type=Path, help="translated markdown")
    ap.add_argument("--lang", default="zh-Hant", help="target language tag")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    findings = check(
        args.source.read_text(encoding="utf-8"),
        args.translated.read_text(encoding="utf-8"),
        args.lang,
    )
    failures = [f for f in findings if f.severity == "fail"]
    if not args.quiet:
        for f in findings:
            print(f)
        if not findings:
            print(f"OK  {args.translated.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
