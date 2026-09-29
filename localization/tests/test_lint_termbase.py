#!/usr/bin/env python3
"""Tests for the termbase lint.

The lint's job is to catch script leakage between the two Chinese columns —
a Simplified character sitting in the Traditional column, or the reverse.
That is invisible when skimming 200 rows and obvious to a reader in Hong Kong.

Run: python3 -m pytest localization/tests/ -q
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "localization" / "glossary"))

from lint_termbase import lint  # noqa: E402

TERMBASE = REPO / "localization" / "glossary" / "zh-termbase.json"


def base_entry(**over):
    e = {"en": "Alpha", "hant": "測試", "hans": "测试", "kind": "term"}
    e.update(over)
    return e


def tb(*entries, keep=None):
    return {"entries": list(entries), "keep_as_is": keep or []}


@pytest.mark.skipif(not TERMBASE.exists(), reason="termbase not present")
def test_shipped_termbase_is_clean():
    assert lint(json.loads(TERMBASE.read_text(encoding="utf-8"))) == []


@pytest.mark.skipif(not TERMBASE.exists(), reason="termbase not present")
def test_termbase_covers_the_high_frequency_boilerplate():
    """The fields that appear in nearly every document must be pinned."""
    entries = json.loads(TERMBASE.read_text(encoding="utf-8"))["entries"]
    pinned = {e["en"] for e in entries}
    for required in ("Document Control", "Document ID", "Classification",
                     "Status", "Version History", "Version", "Roles and Responsibilities",
                     "Purpose", "Scope", "Definitions", "Evidence"):
        assert required in pinned, f"{required} is not in the termbase"


def test_clean_pair_passes():
    assert lint(tb(base_entry())) == []


def test_simplified_char_in_hant_column_is_caught():
    errors = lint(tb(base_entry(hant="测试文档", hans="测试文档")))
    assert any("Simplified characters in hant" in e for e in errors), errors


def test_traditional_char_in_hans_column_is_caught():
    # Columns differ, so the identical-columns rule is not what fires here:
    # the Traditional-only 檔 sitting in the hans column is.
    errors = lint(tb(base_entry(hant="文件", hans="文檔")))
    assert any("Traditional characters in hans" in e for e in errors), errors


def test_high_frequency_iso_pairs_are_covered():
    """Regression guard for the gap this suite found: 驗/验 was unchecked."""
    for simplified, traditional in (("测", "測"), ("试", "試"), ("验", "驗"),
                                    ("读", "讀"), ("个", "個"), ("时", "時")):
        # Simplified char wrongly left in the Traditional column.
        errors = lint(tb(base_entry(hant=f"測試{simplified}", hans="测试字")))
        assert any(simplified in e and "hant" in e for e in errors), \
            f"{simplified} not detected in the hant column: {errors}"
        # Traditional char wrongly pasted into the Simplified column.
        errors = lint(tb(base_entry(hant="測字", hans=f"测试{traditional}")))
        assert any(traditional in e and "hans" in e for e in errors), \
            f"{traditional} not detected in the hans column: {errors}"


def test_identical_columns_must_be_declared():
    errors = lint(tb(base_entry(hant="加密", hans="加密")))
    assert any('set "same": true' in e for e in errors), errors
    assert lint(tb(base_entry(hant="加密", hans="加密", same=True))) == []


def test_false_same_flag_is_caught():
    errors = lint(tb(base_entry(same=True)))
    assert any("marked same:true but columns differ" in e for e in errors), errors


def test_duplicate_same_kind_is_caught():
    errors = lint(tb(base_entry(), base_entry()))
    assert any("duplicate" in e for e in errors), errors


def test_same_term_may_carry_two_senses():
    """'Classification' the label and 'classification' the term are both valid.

    Each must carry a note: the two columns alone cannot show whether a split
    is deliberate or a stale duplicate.
    """
    entries = [
        base_entry(en="Classification", kind="label",
                   hant="機密等級", hans="密级",
                   note="Holds Internal / Confidential / Public."),
        base_entry(en="classification", kind="term",
                   hant="分類", hans="分类",
                   note="The generic act of classifying."),
    ]
    assert lint(tb(*entries)) == []


def test_second_sense_without_a_note_is_caught():
    """A same-named entry that does not say how it differs is a trap.

    Reading the two columns cannot distinguish a deliberate second sense from
    a stale duplicate, and an ad-hoc query keyed on `en` alone silently returns
    whichever entry it saw last — which is how 機密等級 nearly became 分類 in
    the Document Control table.
    """
    entries = [
        base_entry(en="Classification", kind="label",
                   hant="機密等級", hans="密级"),
        base_entry(en="classification", kind="term",
                   hant="分類", hans="分类"),
    ]
    errors = lint(tb(*entries))
    assert sum("has no note explaining" in e for e in errors) == 2, errors


def test_term_also_in_keep_as_is_is_caught():
    errors = lint(tb(base_entry(en="ISO 27001"), keep=["ISO 27001"]))
    assert any("keep_as_is" in e for e in errors), errors


def test_missing_field_is_caught():
    errors = lint(tb({"en": "Alpha", "hant": "測試", "kind": "term"}))
    assert any("empty 'hans'" in e or "missing or empty 'hans'" in e
               for e in errors), errors


def test_bad_kind_is_caught():
    errors = lint(tb(base_entry(kind="sentence")))
    assert any("not in" in e for e in errors), errors
