#!/usr/bin/env python3
"""Tests for the Traditional -> Simplified derivation.

Two things here are not obvious and are pinned so they cannot regress:

* OpenCC alone produces the wrong Simplified for this corpus, because it
  converts glyphs without knowing Taiwan IT vocabulary (網路 -> 网路, not
  网络). The termbase pass is what fixes that.
* The termbase pass must run BEFORE OpenCC. Run the other way round, OpenCC
  rewrites 網路 to 网路 and the termbase key no longer matches anything.

Run: python3 -m pytest localization/tests/ -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "localization"))

import pipeline  # noqa: E402

opencc = pytest.importorskip("opencc", reason="opencc not installed")
CC = opencc.OpenCC("t2s")

TERMBASE = pipeline.load_termbase()

# Traditional input and the Simplified the corpus should end up with.
WANTED = {
    "資訊安全": "信息安全",
    "網路": "网络",
    "軟體": "软件",
    "稽核": "审计",
    "矯正措施": "纠正措施",
    "風險評鑑": "风险评估",
    "個人資料": "个人数据",
    "營運持續": "业务连续性",
    "存取控制": "访问控制",
    "訓練": "培训",
    "認知": "意识",
    "合約": "合同",
}


@pytest.mark.parametrize("hant,hans", sorted(WANTED.items()))
def test_termbase_decides_industry_vocabulary(hant, hans):
    assert pipeline.to_hans(hant, TERMBASE, CC) == hans


def test_opencc_alone_would_be_wrong():
    """The reason the termbase pass exists, stated as a failing baseline."""
    wrong = {"網路": "网路", "軟體": "软体", "稽核": "稽核", "矯正措施": "矫正措施"}
    for hant, bad in wrong.items():
        assert CC.convert(hant) == bad
        assert pipeline.to_hans(hant, TERMBASE, CC) != bad


def test_termbase_must_run_before_opencc():
    """OpenCC first destroys the termbase keys and yields the wrong output."""
    hant = "網路與軟體"
    correct = pipeline.to_hans(hant, TERMBASE, CC)
    assert correct == "网络与软件"

    # The wrong order, spelled out: convert first, then look up.
    lookup = {e["hant"]: e["hans"] for e in TERMBASE["entries"]}
    reversed_order = "".join(lookup.get(ch, ch) for ch in CC.convert(hant))
    assert reversed_order == "网路与软体", reversed_order
    assert reversed_order != correct


def test_longest_term_wins():
    """資訊 must not eat into 資訊安全."""
    assert pipeline.to_hans("資訊安全", TERMBASE, CC) == "信息安全"
    assert pipeline.to_hans("資訊", TERMBASE, CC) == "信息"


def test_non_term_text_still_converts():
    """Residue outside the termbase is OpenCC's job."""
    assert pipeline.to_hans("這個政策涵蓋範圍", TERMBASE, CC) == "这个政策涵盖范围"


def test_watermark_suffix_is_flipped():
    text = "<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-ZH-TW:operational:OP-POL:a.8.9 -->"
    out = pipeline.flip_watermark(text, "zh-TW", "zh-CN")
    assert "ISMS-OP-POL-A.8.9-ZH-CN:" in out
    assert "ZH-TW" not in out


def test_watermark_flip_leaves_document_id_untouched():
    """Only the watermark carries the suffix; a bare doc ID must stay bare."""
    text = ("<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-ZH-TW:operational:OP-POL:a.8.9 -->\n"
            "| **文件編號** | ISMS-OP-POL-A.8.9 |\n")
    out = pipeline.flip_watermark(text, "zh-TW", "zh-CN")
    assert "| **文件編號** | ISMS-OP-POL-A.8.9 |" in out


def test_derivation_preserves_line_count(tmp_path):
    hant = tmp_path / "zh-TW" / "ISMS-OP-POL-T.1 - 範例 - ZH-TW.md"
    hant.parent.mkdir(parents=True)
    hant.write_text(
        "<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-TW:operational:OP-POL:t.1 -->\n"
        "**ISMS-OP-POL-T.1 — 範例控制措施**\n\n"
        "## 目的\n\n本政策說明資訊安全與網路的要求。\n",
        encoding="utf-8",
    )
    out = pipeline.derive_simplified(hant, termbase=TERMBASE)
    assert out.name == "ISMS-OP-POL-T.1 - 範例 - ZH-CN.md"
    # Sibling of zh-TW, not nested inside it: assert on the grandparent too,
    # or an IMP/zh-TW/zh-CN path would satisfy a check on .parent.name alone.
    assert out.parent.name == "zh-CN"
    assert out.parent.parent == hant.parent.parent
    assert out.parent.parent.name != "zh-TW"
    derived = out.read_text(encoding="utf-8")
    assert derived.count("\n") + 1 == hant.read_text(encoding="utf-8").count("\n") + 1
    assert "信息安全" in derived and "网络" in derived
    assert "ISMS-OP-POL-T.1-ZH-CN:" in derived


def test_derived_text_has_no_traditional_only_characters(tmp_path):
    """A derived file must be clean Simplified, not half-converted."""
    sys.path.insert(0, str(REPO / "localization" / "glossary"))
    from lint_termbase import TRADITIONAL_ONLY

    hant = tmp_path / "zh-TW" / "doc - ZH-TW.md"
    hant.parent.mkdir(parents=True)
    hant.write_text(
        "<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-TW:operational:OP-POL:t.1 -->\n"
        "**ISMS-OP-POL-T.1 — 測試文件**\n\n## 範圍\n\n稽核與矯正措施，營運持續。\n",
        encoding="utf-8",
    )
    out = pipeline.derive_simplified(hant, termbase=TERMBASE)
    derived = out.read_text(encoding="utf-8")
    leaked = sorted(set(derived) & TRADITIONAL_ONLY)
    assert not leaked, f"Traditional characters survived derivation: {''.join(leaked)}"


def test_line_count_regression_is_rejected(tmp_path):
    """A term whose replacement contains a newline would break alignment."""
    bad = {"entries": [{"en": "x", "hant": "測試", "hans": "测\n试",
                        "kind": "term"}]}
    hant = tmp_path / "zh-TW" / "doc - ZH-TW.md"
    hant.parent.mkdir(parents=True)
    hant.write_text("測試\n測試\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line count"):
        pipeline.derive_simplified(hant, termbase=bad)


def test_target_path_follows_the_convention():
    en = REPO / ("isms-core-operational/A.8-technological-controls/"
                 "isms-a.8.9-configuration-management/POL/"
                 "ISMS-OP-POL-A.8.9 - Configuration Management.md")
    got = pipeline.target_path(en, "zh-TW", "組態管理")
    assert got.name == "ISMS-OP-POL-A.8.9 - Configuration Management - 組態管理 - ZH-TW.md" or \
           got.name.endswith(" - 組態管理 - ZH-TW.md")
    assert got.parent.name == "zh-TW"
    assert got.parent.parent.name == "POL"


def test_audit_counts_real_packs():
    report = pipeline.audit(["isms-core-operational"])
    assert report["english_documents"] > 40
    assert report["languages"]["de"] > 40
    assert report["languages"]["zh-TW"] == 0


# --- CLI entry points -------------------------------------------------------
# The functions above are the tested units, so a break in the argument wiring
# between main() and them stays invisible: `derive` shipped reading args.pack,
# which only plan and audit declare, and crashed on every invocation.

def test_cli_derive_writes_the_simplified_sibling(tmp_path, capsys):
    hant = tmp_path / "zh-TW" / "ISMS-OP-POL-T.1 - 範例 - ZH-TW.md"
    hant.parent.mkdir(parents=True)
    hant.write_text(
        "<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-TW:operational:OP-POL:t.1 -->\n"
        "**ISMS-OP-POL-T.1 — 範例**\n\n本政策說明資訊安全。\n",
        encoding="utf-8",
    )
    assert pipeline.main(["derive", str(hant)]) == 0
    out = hant.parent.parent / "zh-CN" / "ISMS-OP-POL-T.1 - 範例 - ZH-CN.md"
    assert out.exists(), capsys.readouterr().out
    assert "信息安全" in out.read_text(encoding="utf-8")


def test_cli_plan_lists_pending_and_exits_zero(capsys):
    assert pipeline.main(["plan", "--pack", "isms-core-operational",
                          "--lang", "zh-TW"]) == 0
    out = capsys.readouterr().out
    assert "pending for zh-TW" in out


def test_cli_audit_reports_coverage(capsys):
    assert pipeline.main(["audit", "--pack", "isms-core-operational"]) == 0
    out = capsys.readouterr().out
    assert "English documents:" in out
    assert "Translated in no language:" in out


def test_coordinated_term_beats_its_own_component():
    """A term inside a coordination must still be substituted as a whole.

    'risk assessment and treatment' is 風險評鑑與處理 in Traditional, and the
    mainland rendering of 'risk treatment' alone is 风险处置 — deliberately,
    not 风险处理, which is the plain OpenCC output. The entry for 'risk
    treatment' keys on the contiguous 風險處理, so the coordinated form never
    matched it and only the residual 處理 reached OpenCC, which renders it
    处理. One Simplified file then carried 风险处置 for the ISO term and
    处理程序 for the same concept (CLD-SEC-POL-A.5.38). Entries are applied
    longest-first, so an entry for the coordinated form wins over both parts.
    """
    assert pipeline.to_hans("風險評鑑與處理程序", TERMBASE, CC) == "风险评估与处置程序"
    # The verb sense must not be dragged along by the term entry.
    assert pipeline.to_hans("風險予以處理", TERMBASE, CC) == "风险予以处理"
