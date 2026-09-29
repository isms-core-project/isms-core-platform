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

import re
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


def test_single_character_keys_are_not_substituted():
    """A one-character key cannot be applied without word boundaries.

    得 -> 可 is a correct glossary entry (得 is the Traditional modal "may")
    and still rewrote 取得, "to obtain", as 取可 in a shipped Simplified file.
    Substitution is an alternation over raw text — Chinese has no word
    boundaries to anchor on — so a one-character key fires inside every word
    that happens to contain the character.

    Such entries stay in the termbase as guidance for translators and are held
    back from derivation. Nothing is lost: 得 is glyph-neutral, so the residue
    pass leaves it alone and the Simplified keeps the 得 that was always
    correct there.
    """
    assert pipeline.to_hans("取得 CSP 提出的資訊", TERMBASE, CC) == "取得 CSP 提出的信息"
    assert pipeline.to_hans("長得快", TERMBASE, CC) == "长得快"
    # 欄 is held back too. It is safe in this corpus only because the longer
    # entry 欄位 -> 字段 matches first; that is luck, not a guarantee.
    assert pipeline.to_hans("欄位", TERMBASE, CC) == "字段"

    held_back = {e["hant"] for e in TERMBASE["entries"]} - \
                {e["hant"] for e in pipeline.derivable(TERMBASE)}
    assert held_back == {"欄", "得", "值", "高", "中", "低", "是", "否", "應", "宜"}, \
        f"the set of held-back single-character keys changed: {sorted(held_back)}"


def test_derivable_keeps_every_multi_character_entry():
    """The rule is about key length only — it must not quietly drop real terms."""
    derivable = {e["hant"] for e in pipeline.derivable(TERMBASE)}
    for hant in ("資訊安全", "稽核", "風險評鑑與處理", "聯絡窗口", "組態", "欄位"):
        assert hant in derivable, hant


def test_a_key_with_two_senses_is_not_in_the_termbase():
    """重大 is 'material' in 重大變更 and 'Critical' only as a severity value.

    Mapping it to 严重 rewrote all seven material-change occurrences in the
    corpus as 严重变更 — the exact mistake that looks like a translation win.
    Severity is written 嚴重 on the Traditional side, which OpenCC converts on
    its own, so the entry had nothing to do.
    """
    assert pipeline.to_hans("重大變更", TERMBASE, CC) == "重大变更"
    assert pipeline.to_hans("嚴重 CVE", TERMBASE, CC) == "严重 CVE"
    assert not any(e["hant"] == "重大" for e in TERMBASE["entries"])


def test_derived_corpus_has_no_broken_words():
    """End-to-end guard: derive every shipped Traditional file and look for the
    damage patterns the held-back keys used to produce."""
    broken = re.compile("取可|严重变更|可力|可到")
    sources = [p for p in (REPO / "isms-core-cloud").rglob("*.md")
               if p.parent.name == "zh-TW"]
    sources += list(REPO.glob("*.zh-TW.md"))
    assert sources, "no Traditional sources found — has the corpus moved?"
    for path in sources:
        derived = pipeline.to_hans(path.read_text(encoding="utf-8"), TERMBASE, CC)
        for n, line in enumerate(derived.splitlines(), 1):
            assert not broken.search(line), f"{path.name}:{n}: {line.strip()}"


def test_residue_converter_may_not_override_the_termbase():
    """The residue pass runs last, so it must only convert glyphs, never words.

    Swapping t2s for tw2sp looks like a quality upgrade: it is word-aware for
    Taiwan vocabulary and it did earn two real termbase entries (聯絡窗口 ->
    联系窗口 and 組態 -> 配置, the latter it does not fix either). But it also
    contradicts terms the termbase has already decided — 程序 'procedure', an
    entry deliberately declared identical in both scripts, becomes 进程 (an OS
    process); 核心原則 becomes 内核原則 (a kernel). Running last, it wins every
    such disagreement silently, and a dictionary is the wrong layer to overrule
    a reviewed decision.

    So the converter is pinned by behaviour rather than by name. Two groups
    below: the strings the two dictionaries disagree on, and the gaps that were
    closed in the termbase instead — for those, the termbase runs first, so
    both converters agree and the cheaper fix carries no risk at all.
    """
    tw2sp = opencc.OpenCC("tw2sp")

    # Where tw2sp disagrees with a curated decision. Because it runs last, each
    # of these would silently win. The fixed strings say what the shipped
    # pipeline must keep producing.
    for hant, shipped in (
        ("程序", "程序"),          # termbase entry, declared same in both scripts
        ("文件標題", "文件标题"),    # ditto — tw2sp says 文档标题
        ("核心原則", "核心原则"),    # residue prose — tw2sp says 内核原则 (a kernel)
    ):
        got = pipeline.to_hans(hant, TERMBASE, CC)
        assert got == shipped, f"shipped converter now yields {got!r} for {hant}"
        assert pipeline.to_hans(hant, TERMBASE, tw2sp) != shipped, (
            f"{hant} no longer demonstrates the tw2sp hazard — re-check whether "
            f"switching the residue converter is now safe"
        )

    # Gaps closed in the termbase rather than by the converter. 稽核 is the ISO
    # mainland term 审计, not the generic 审核 tw2sp would give; 聯絡窗口 and
    # 組態 are Taiwan phrasings OpenCC leaves alone. All three now resolve
    # before either converter sees them.
    for hant, hans in (("稽核", "审计"), ("聯絡窗口", "联系窗口"), ("組態", "配置")):
        assert pipeline.to_hans(hant, TERMBASE, CC) == hans
        assert pipeline.to_hans(hant, TERMBASE, tw2sp) == hans


# --- Repository documents (README.md and friends) ---------------------------
# These are the only files localized in place rather than under a language
# directory, and the only ones carrying a language line.

def test_switcher_marks_exactly_the_current_language():
    sys.path.insert(0, str(REPO / "localization" / "glossary"))
    from charsets import LANGUAGE_LINE_RE

    for lang in pipeline.SWITCHER_LANGS:
        line = pipeline.switcher("README", lang)
        assert line.count("<strong>") == 1, line
        assert f"<strong>{pipeline.LANGUAGE_NAMES[lang]}</strong>" in line, line
        # Every other variant is a link to its own file.
        for other in pipeline.SWITCHER_LANGS:
            if other == lang:
                continue
            href = "README.md" if other == "en" else f"README.{other}.md"
            assert f'href="{href}"' in line, line
        # The script gate has to recognise this line in all three spellings, or
        # every localized repository document fails the script check in both
        # directions — 简体中文 in the Traditional file and 繁體中文 in the
        # Simplified one are correct there and nowhere else. Anchored on the
        # markup, so the two modules have to agree on the shape, not just on
        # the words: this assertion is the seam.
        assert LANGUAGE_LINE_RE.match(line), line


def test_derived_repository_document_keeps_the_language_line_intact(tmp_path):
    """The language names are not translated, so t2s must not touch them.

    A reader looks for their own label in their own characters. Converting the
    line would leave the Simplified copy advertising 繁体中文 — a label nobody
    searches for — while the prose around it converts normally.
    """
    src = tmp_path / "README.zh-TW.md"
    src.write_text(
        pipeline.switcher("README", "zh-TW") + "\n\n## 範圍\n\n資訊安全與風險評鑑。\n",
        encoding="utf-8",
    )
    out = pipeline.derive_doc(src, termbase=TERMBASE)
    assert out.name == "README.zh-CN.md"
    assert out.parent == src.parent       # side by side, not in a subdirectory
    text = out.read_text(encoding="utf-8")
    assert pipeline.switcher("README", "zh-CN") in text
    assert "繁體中文" in text             # the other variant's own label, kept
    assert "繁体中文" not in text
    assert "信息安全与风险评估" in text    # the prose did convert


def test_derived_repository_document_links_to_its_own_siblings(tmp_path):
    """Cross-links carry a language tag, and the tag means "mine".

    A link in README.zh-TW.md to PARADIGM.zh-TW.md reads as "the Traditional
    PARADIGM" — from the Simplified copy the same sentence has to reach
    PARADIGM.zh-CN.md, or every cross-link in the derived tree lands on the
    wrong script. Link text and target are written the same way, so one
    substitution moves both.
    """
    src = tmp_path / "README.zh-TW.md"
    src.write_text(
        pipeline.switcher("README", "zh-TW")
        + "\n\n請先讀 [PARADIGM.zh-TW.md](PARADIGM.zh-TW.md)，"
          "或英文的 [PLATFORM.md](PLATFORM.md)。\n",
        encoding="utf-8",
    )
    out = pipeline.derive_doc(src, termbase=TERMBASE)
    text = out.read_text(encoding="utf-8")
    assert "[PARADIGM.zh-CN.md](PARADIGM.zh-CN.md)" in text
    assert "[PLATFORM.md](PLATFORM.md)" in text      # English targets untouched
    # The switcher is the one link that must keep pointing the other way.
    assert text.count(".zh-TW.md") == 1, text


def test_derive_doc_requires_a_language_line(tmp_path):
    src = tmp_path / "PLATFORM.zh-TW.md"
    src.write_text("## 範圍\n\n沒有語言列。\n", encoding="utf-8")
    with pytest.raises(ValueError, match="no language line"):
        pipeline.derive_doc(src, termbase=TERMBASE)


def test_derive_doc_rejects_a_simplified_source(tmp_path):
    src = tmp_path / "README.zh-CN.md"
    src.write_text(pipeline.switcher("README", "zh-CN") + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="not a zh-TW repository document"):
        pipeline.derive_doc(src, termbase=TERMBASE)


def test_cli_derive_doc_writes_the_sibling(tmp_path):
    src = tmp_path / "README.zh-TW.md"
    src.write_text(
        pipeline.switcher("README", "zh-TW") + "\n\n## 範圍\n\n資訊安全。\n",
        encoding="utf-8",
    )
    assert pipeline.main(["derive-doc", str(src)]) == 0
    out = src.with_name("README.zh-CN.md")
    assert out.exists()
    assert pipeline.switcher("README", "zh-CN") in out.read_text(encoding="utf-8")
