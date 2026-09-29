#!/usr/bin/env python3
"""Tests for the script-specific character sets.

These sets decide whether a translated document is written in one script or
an accidental mixture of two, so a wrong entry is expensive in both
directions: too narrow and a leak ships, too wide and correct text is blocked.

The interesting test is `test_every_leak_in_the_repo_is_covered`. It re-derives
candidates from the Chinese documents actually on disk using OpenCC, subtracts
what the curated sets already know, and fails on the remainder. That is how
the sets grow: the gate stays precise, and this test finds the gaps instead of
a reader in Hong Kong finding them.

Run: python3 -m pytest localization/tests/ -q
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "localization" / "glossary"))

import charsets  # noqa: E402
from charsets import (KNOWN_SHARED, SIMPLIFIED_ONLY, TRADITIONAL_ONLY,  # noqa: E402
                      leak_candidates, leaks, uncovered)

opencc = pytest.importorskip("opencc", reason="opencc not installed")

REPO_DOC_RE = re.compile(r"\.(?P<lang>zh-TW|zh-CN)\.md$")


def chinese_documents() -> list[tuple[Path, str]]:
    """Every Chinese document in the checkout, paired with its language.

    The repo has two layouts and both have to be scanned. Content packs keep
    translations in a language directory (POL/zh-TW/…), while the repository
    documents sit next to their English original (README.zh-TW.md). Scanning
    only the first — which is all this did at first — leaves the whole second
    class outside the net, and those are the files most likely to carry the
    language line that this module now exempts.
    """
    out: list[tuple[Path, str]] = []
    for d in REPO.glob("isms-core-*"):
        out.extend((p, p.parent.name) for p in d.rglob("*.md")
                   if p.parent.name in ("zh-TW", "zh-CN"))
    for p in REPO.glob("*.md"):
        m = REPO_DOC_RE.search(p.name)
        if m:
            out.append((p, m.group("lang")))
    return sorted(out)


# --------------------------------------------------------------------------
# The shipped sets must be internally sound.
# --------------------------------------------------------------------------

def test_shipped_charsets_are_script_specific():
    """Every listed character is really script-specific, per OpenCC."""
    assert charsets.check_against_opencc() == []


def test_no_character_is_claimed_by_both_sets():
    assert not (SIMPLIFIED_ONLY & TRADITIONAL_ONLY)


def test_known_shared_is_not_also_in_a_script_set():
    assert not (KNOWN_SHARED & (SIMPLIFIED_ONLY | TRADITIONAL_ONLY))


# --------------------------------------------------------------------------
# Detection behaviour.
# --------------------------------------------------------------------------

def test_valid_traditional_text_has_no_leaks():
    """The words that make this check hard must not fire.

    准/台/週/系/制/面 are all correct Traditional and all have a Simplified
    twin, so a blunt per-character OpenCC test would flag every one of them.
    """
    text = "核准的標準；平台與週期；周圍與周詳；內容與系統；控制與方面"
    assert leaks(text, "zh-TW") == {}


def test_valid_simplified_text_has_no_leaks():
    text = "核准的标准；平台与周期；周围与周详；内容与系统；控制与方面"
    assert leaks(text, "zh-CN") == {}


def test_hou_is_flagged_in_traditional_by_design():
    """A deliberate false positive, pinned so it stays deliberate.

    皇后 is legitimate Traditional, but in governance prose 后 is overwhelmingly
    a typo for 後 — too common to leave unflagged, too rare to matter the other
    way. See the note in charsets.py.
    """
    assert "后" in leaks("皇后", "zh-TW")


def test_simplified_character_in_traditional_text_is_reported_with_lines():
    # The surrounding text is genuinely Traditional — 這個, not 这个 — so the
    # only findings are the two injected ones, one of them on two lines.
    text = "第一行正常\n第二行有发现這個詞\n第三行又有发\n"
    found = leaks(text, "zh-TW")
    assert set(found) == {"发", "现"}
    assert found["发"] == [2, 3]
    assert found["现"] == [2]


def test_traditional_character_in_simplified_text_is_reported():
    found = leaks("这是正確的記錄\n", "zh-CN")
    assert "確" in found and "錄" in found


def test_unknown_language_checks_nothing():
    """German and English documents must not be run through a Chinese check."""
    assert leaks("發現发現", "de") == {}
    assert leaks("發現发現", "en") == {}


@pytest.mark.parametrize("tag", ["zh-TW", "zh-Hant", "zh-HK", "zh_TW"])
def test_every_traditional_tag_spelling_is_recognised(tag):
    """A gate keyed on one spelling only would silently skip the others."""
    assert "发" in leaks("发现", tag), f"{tag} not recognised"


@pytest.mark.parametrize("tag", ["zh-CN", "zh-Hans", "zh-SG"])
def test_every_simplified_tag_spelling_is_recognised(tag):
    assert "發" in leaks("發現", tag), f"{tag} not recognised"


# --------------------------------------------------------------------------
# The coverage net: find gaps in the curated sets from real documents.
# --------------------------------------------------------------------------

def test_every_leak_in_the_repo_is_covered():
    """No Chinese document contains a stray character the gate would miss.

    Runs in both directions: Traditional documents are scanned for Simplified
    characters and Simplified documents for Traditional ones, so a gap in
    either set surfaces here.
    """
    docs = chinese_documents()
    if not docs:
        pytest.skip("no Chinese documents in this checkout yet")
    s2t, t2s = opencc.OpenCC("s2t"), opencc.OpenCC("t2s")
    missing: dict[str, set[str]] = {}
    for path, lang in docs:
        cands = leak_candidates(path.read_text(encoding="utf-8"), lang, s2t, t2s)
        gap = uncovered(cands, lang)
        if gap:
            missing[str(path.relative_to(REPO))] = gap
    assert not missing, (
        f"characters the gate would let through in {len(missing)} of "
        f"{len(docs)} document(s) — add them to charsets.py or to "
        f"KNOWN_SHARED with a reason:\n"
        + "\n".join(f"  {p}: {''.join(sorted(g))}" for p, g in sorted(missing.items()))
    )


def test_coverage_net_actually_finds_a_known_gap():
    """The net above is only worth having if it can fail."""
    assert uncovered({"发", "现"}, "zh-TW") == set()
    assert uncovered({"龘"}, "zh-TW") == {"龘"}
    assert uncovered({"發", "現"}, "zh-CN") == set()


def test_coverage_net_is_direction_aware():
    """A Simplified document's own characters are not candidates."""
    s2t, t2s = opencc.OpenCC("s2t"), opencc.OpenCC("t2s")
    hans = "这是一份简体文件，包含密钥与字符串。"
    assert leak_candidates(hans, "zh-CN", s2t, t2s) == set()
    assert leak_candidates(hans, "zh-TW", s2t, t2s) != set()


# --------------------------------------------------------------------------
# The language line: the one place both scripts belong in the same file.
# --------------------------------------------------------------------------

# Canonical shape, as emitted by pipeline.switcher. The order is fixed —
# English, then 繁體中文, then 简体中文 — which is what lets one pattern
# recognise the line in all three of its spellings.
LANG_LINE = ('<p align="center"><a href="README.md">English</a> · '
             '<strong>繁體中文</strong> · '
             '<a href="README.zh-CN.md">简体中文</a></p>')


def test_language_line_is_not_a_leak_in_either_direction():
    """Each variant is named in its own characters, so both files trip the gate.

    A reader looks for their own label in their own script — 繁體中文 is not
    translated to 繁体中文 and 简体中文 is not rendered as 簡體中文 — which
    puts Simplified characters in the Traditional file and Traditional ones in
    the Simplified file. Read literally the gate would call that line a leak in
    both directions at once, so the line is exempt.
    """
    assert charsets.LANGUAGE_LINE_RE.match(LANG_LINE)

    assert leaks(LANG_LINE, "zh-TW") == {}   # 简体中文 sits here on purpose
    assert leaks(LANG_LINE, "zh-CN") == {}   # and 繁體中文 on the other side

    # It is the line that is exempt, not the characters. The same glyphs
    # anywhere else still fail — otherwise this would be a hole big enough to
    # drive a real leak through.
    assert "简" in leaks("简体中文是简体字。\n", "zh-TW")
    assert "简" in leaks(LANG_LINE + "\n简体中文是简体字。\n", "zh-TW")


def test_language_line_stays_out_of_the_coverage_audit():
    """Left in, its characters would read as permanent gaps in the sets.

    简 and 体 are correctly Simplified-only and correctly present in a
    Traditional README, so the net would report them as characters the gate
    fails to catch, on every run, forever.
    """
    s2t, t2s = opencc.OpenCC("s2t"), opencc.OpenCC("t2s")
    assert leak_candidates(LANG_LINE, "zh-TW", s2t, t2s) == set()
    assert leak_candidates(LANG_LINE, "zh-CN", s2t, t2s) == set()
    # The same text without the markup is still audited.
    assert leak_candidates("简体中文", "zh-TW", s2t, t2s) != set()


def test_a_document_that_looks_like_the_language_line_is_still_audited():
    """The exemption is anchored on the markup, not on the words.

    A prose line mentioning both scripts in a <p> is not a language line
    unless it is the centred switcher, so it must keep being checked.
    """
    prose = "<p>繁體中文與简体中文的對照表</p>"
    assert not charsets.LANGUAGE_LINE_RE.match(prose)
    assert "简" in leaks(prose, "zh-TW")


def test_canonical_collapses_the_bcp47_synonyms():
    """zh-Hant and zh-TW name the same tree; the repo writes the short form.

    The CLI accepts --lang zh-Hant because it is the correct BCP-47 spelling,
    and that used to be the default. A gate that then predicted a watermark
    suffix of ZH-HANT flagged every correct document it was given, because no
    file in the repository carries that suffix — the tag has to collapse to the
    spelling the repo actually writes before it is used to build one.
    """
    assert charsets.canonical("zh-Hant") == "zh-TW"
    assert charsets.canonical("zh-Hans") == "zh-CN"
    assert charsets.canonical("zh_TW") == "zh-TW"      # underscore variant
    assert charsets.canonical("ZH-CN") == "zh-CN"      # case-insensitive
    assert charsets.canonical("zh-TW") == "zh-TW"      # already canonical
    # An unknown tag has no canonical form to invent, so it passes through and
    # the caller sees the name they typed in any error message.
    assert charsets.canonical("ja") == "ja"


def test_every_accepted_tag_has_a_canonical_form():
    """A tag the script gate honours but canonical() ignores would be a hole."""
    for tag in charsets.TRADITIONAL_TAGS + charsets.SIMPLIFIED_TAGS:
        assert charsets.canonical(tag) in ("zh-TW", "zh-CN"), tag
