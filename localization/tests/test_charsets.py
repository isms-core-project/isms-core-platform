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

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "localization" / "glossary"))

import charsets  # noqa: E402
from charsets import (KNOWN_SHARED, SIMPLIFIED_ONLY, TRADITIONAL_ONLY,  # noqa: E402
                      leak_candidates, leaks, uncovered)

opencc = pytest.importorskip("opencc", reason="opencc not installed")


def chinese_documents() -> list[Path]:
    """Every zh-TW / zh-CN document currently in the checkout."""
    out: list[Path] = []
    for d in REPO.glob("isms-core-*"):
        out.extend(p for p in d.rglob("*.md") if p.parent.name in ("zh-TW", "zh-CN"))
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
    for path in docs:
        lang = path.parent.name
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
