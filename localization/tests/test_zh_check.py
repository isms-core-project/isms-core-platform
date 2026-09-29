#!/usr/bin/env python3
"""Tests for the Chinese localization gate.

Two ground truths anchor these tests:

* Positive — the real English/German pair shipped in the repository
  (ISMS-OP-POL-A.8.9) is structurally line-aligned. A gate that fails it is
  too strict.
* Negative — upstream PR #2's Turkish localization was closed for shipping
  1240 files of exactly 33 lines of template filler with English titles.
  A gate that passes that is too weak.

Run: python3 -m pytest localization/tests/ -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "localization"))

from zh_check import check, main  # noqa: E402

A89_DIR = REPO / (
    "isms-core-operational/A.8-technological-controls/"
    "isms-a.8.9-configuration-management/POL"
)
EN_DOC = A89_DIR / "ISMS-OP-POL-A.8.9 - Configuration Management.md"
DE_DOC = A89_DIR / "de/ISMS-OP-POL-A.8.9 - Konfigurationsmanagement - DE.md"


def gates(findings):
    return {f.gate for f in findings}


# --------------------------------------------------------------------------
# Positive: the real German translation must clear the structural gates.
# --------------------------------------------------------------------------

@pytest.mark.skipif(not (EN_DOC.exists() and DE_DOC.exists()),
                    reason="reference pair not present in this checkout")
def test_real_pair_is_structurally_aligned():
    findings = check(EN_DOC.read_text(encoding="utf-8"),
                     DE_DOC.read_text(encoding="utf-8"), lang="de")
    assert "structure" not in gates(findings), [str(f) for f in findings]
    assert "identifier" not in gates(findings), [str(f) for f in findings]


@pytest.mark.skipif(not (EN_DOC.exists() and DE_DOC.exists()),
                    reason="reference pair not present in this checkout")
def test_real_pair_sets_stub_size_baseline():
    """Sanity: the fixture is big enough for the stub rule to be meaningful."""
    src = EN_DOC.read_text(encoding="utf-8")
    assert src.count("\n") > 100


# --------------------------------------------------------------------------
# Negative: PR #2's failure mode must be caught.
# --------------------------------------------------------------------------

PR2_STUB = """<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-TR:operational:OP-POL:a.8.9 -->
# ISMS-OP-POL-A.8.9

**ISMS-OP-POL-A.8.9 - Configuration Management**

Bu dokuman, kurulusun bilgi varliklarinin gizlilik, butunluk ve
erisilebilirlik ilkeleri dogrultusunda yonetilmesini saglar.

Roller ve sorumluluklar bu politika kapsaminda tanimlanmistir. Ust yonetim
politikanin uygulanmasindan nihai olarak sorumludur. Ilgili tum personel
bu politikaya uymakla yukumludur.

Izleme ve gozden gecirme faaliyetleri duzenli olarak yurutulur. Politikada
yapilacak degisiklikler kontrol altinda tutulur ve kayit altina alinir.
Uygunsuzluklar tespit edildiginde duzeltici faaliyetler baslatilir.
"""


@pytest.mark.skipif(not EN_DOC.exists(), reason="source doc not present")
def test_pr2_style_filler_is_rejected():
    findings = check(EN_DOC.read_text(encoding="utf-8"), PR2_STUB,
                     lang="zh-Hant")
    g = gates(findings)
    assert "substance" in g, [str(f) for f in findings]
    # It is short, it is not Chinese, and it kept the English title.
    assert "stub" in " ".join(str(f) for f in findings)
    assert "CJK ratio" in " ".join(str(f) for f in findings)
    assert "title left in English" in " ".join(str(f) for f in findings)
    assert "structure" in g


# --------------------------------------------------------------------------
# Synthetic pair for the structural gates, kept small and self-contained.
# --------------------------------------------------------------------------

EN_SMALL = """<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1:operational:OP-POL:t.1 -->
# ISMS-OP-POL-T.1

**ISMS-OP-POL-T.1 - Sample Control**

## Purpose

This policy states the purpose.

| **Document ID** | ISMS-OP-POL-T.1 |
| --- | --- |
| **Owner** | CISO |

## Scope

- First requirement
- Second requirement

<!-- QA_VERIFIED: 2026-01-01 -->
"""

# The watermark carries the tag the repository writes (zh-TW), not the BCP-47
# synonym. The calls below deliberately pass lang="zh-Hant" anyway: both
# spellings must name the same tree, so the synonym has to reach the same
# expected suffix. That seam used to be broken in the opposite direction —
# zh-Hant was the CLI default and predicted ZH-HANT, which no file carries, so
# the gate failed every correct document it was handed.
ZH_SMALL = """<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-TW:operational:OP-POL:t.1 -->
# ISMS-OP-POL-T.1

**ISMS-OP-POL-T.1 - 範例控制措施**

## 目的

本政策說明其目的。

| **Document ID** | ISMS-OP-POL-T.1 |
| --- | --- |
| **Owner** | 資訊安全長 |

## 範圍

- 第一項要求
- 第二項要求

<!-- QA_VERIFIED: 2026-01-01 -->
"""


def test_aligned_synthetic_pair_passes():
    assert check(EN_SMALL, ZH_SMALL, lang="zh-Hant") == []


def test_dropped_table_row_is_caught():
    broken = ZH_SMALL.replace("| **Owner** | 資訊安全長 |\n", "")
    findings = check(EN_SMALL, broken, lang="zh-Hant")
    assert "structure" in gates(findings)
    assert "table rows" in " ".join(str(f) for f in findings)


def test_dropped_heading_is_caught():
    broken = ZH_SMALL.replace("## 範圍\n", "")
    findings = check(EN_SMALL, broken, lang="zh-Hant")
    assert "structure" in gates(findings)
    assert "h2 headings" in " ".join(str(f) for f in findings)


def test_line_delta_tolerance():
    plus_one = ZH_SMALL.replace("## 目的\n", "## 目的\n\n")
    assert "structure" not in gates(check(EN_SMALL, plus_one, lang="zh-Hant"))
    plus_three = ZH_SMALL.replace("## 目的\n", "## 目的\n\n\n\n")
    assert "structure" in gates(check(EN_SMALL, plus_three, lang="zh-Hant"))


def test_wrong_watermark_suffix_is_caught():
    broken = ZH_SMALL.replace("ISMS-OP-POL-T.1-ZH-TW:", "ISMS-OP-POL-T.1-ZH:")
    findings = check(EN_SMALL, broken, lang="zh-Hant")
    assert "identifier" in gates(findings)


def test_the_bcp47_synonym_matches_the_repos_own_suffix():
    """--lang zh-Hant and --lang zh-TW must accept the same documents.

    zh-Hant is the correct BCP-47 spelling and used to be the CLI default, so
    the synonym path is not a corner case — it is what a caller gets by
    omitting the flag. It has to collapse to zh-TW before the expected
    watermark suffix is built, or every correctly watermarked file fails.
    """
    assert check(EN_SMALL, ZH_SMALL, lang="zh-Hant") == []
    assert check(EN_SMALL, ZH_SMALL, lang="zh-TW") == []
    # The Simplified side, same contract. Written out rather than derived by
    # string surgery: patching a Traditional fixture in place leaves glyphs the
    # script gate correctly rejects, which would test the patch, not the tag.
    hans = """<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-CN:operational:OP-POL:t.1 -->
# ISMS-OP-POL-T.1

**ISMS-OP-POL-T.1 - 示例控制措施**

## 目的

本政策说明其目的。

| **Document ID** | ISMS-OP-POL-T.1 |
| --- | --- |
| **Owner** | 信息安全长 |

## 范围

- 第一项要求
- 第二项要求

<!-- QA_VERIFIED: 2026-01-01 -->
"""
    assert check(EN_SMALL, hans, lang="zh-Hans") == []
    assert check(EN_SMALL, hans, lang="zh-CN") == []


def test_missing_watermark_is_caught():
    broken = "\n".join(
        ln for ln in ZH_SMALL.splitlines() if not ln.startswith("<!-- ISMS-CORE:")
    )
    assert "identifier" in gates(check(EN_SMALL, broken, lang="zh-Hant"))


def test_missing_qa_footer_blocks_promotion():
    broken = ZH_SMALL.replace("<!-- QA_VERIFIED: 2026-01-01 -->\n", "")
    assert "promotion" in gates(check(EN_SMALL, broken, lang="zh-Hant"))


def test_document_id_value_stays_bare():
    """The control table carries the bare doc ID, not the lang-suffixed one."""
    assert "| **Document ID** | ISMS-OP-POL-T.1 |" in ZH_SMALL


# --------------------------------------------------------------------------
# CLI contract
# --------------------------------------------------------------------------

def test_cli_exit_codes(tmp_path):
    src = tmp_path / "en.md"
    dst = tmp_path / "zh.md"
    src.write_text(EN_SMALL, encoding="utf-8")
    dst.write_text(ZH_SMALL, encoding="utf-8")
    assert main([str(src), str(dst), "--quiet"]) == 0
    dst.write_text(PR2_STUB, encoding="utf-8")
    assert main([str(src), str(dst), "--quiet"]) == 1


# --------------------------------------------------------------------------
# Heading levels beyond ## and ###
# --------------------------------------------------------------------------
# The cloud policy documents put their major sections at level 1. A gate that
# only counted ## and ### would check nothing but the table rows in those
# files, so every level is compared.

CLD_POL_DIR = REPO / ("isms-core-cloud/iso27017-sec-cloud/"
                      "cld-sec-a.5.38-shared-roles-responsibilities/POL")
EN_POL = CLD_POL_DIR / "CLD-SEC-POL-A.5.38 - Shared Roles and Responsibilities.md"
DE_POL = CLD_POL_DIR / ("de/CLD-SEC-POL-A.5.38 - Gemeinsame Rollen und "
                        "Verantwortlichkeiten - DE.md")


def test_dropped_h1_is_caught():
    src = "# Scope and Applicability\n\nBody text.\n"
    dst = ("<!-- ISMS-CORE:POLICY:X-ZH-TW:sec:POL:x -->\n"
           "**X — 範圍**\n\n正文內容。\n<!-- QA_VERIFIED: 2026-01-01 -->\n")
    findings = check(src, dst, lang="zh-TW")
    assert any("h1 headings" in f.detail for f in findings), \
        [str(f) for f in findings]


@pytest.mark.skipif(not (EN_POL.exists() and DE_POL.exists()),
                    reason="cloud policy pair not present in this checkout")
def test_real_h1_policy_pair_is_heading_aligned():
    """Positive control on a real upstream pair that uses level-1 sections.

    Only the heading alignment is asserted. The other gates are out of scope
    here in both directions: the CJK ratio is a Chinese check and will always
    fail a German document, and this pair happens to be one of the ~2% that
    drift by more than one line (176 vs 178). Asserting the whole structure
    gate would pin a tolerance the fixture does not meet, which says nothing
    about whether the heading fix works.
    """
    src = EN_POL.read_text(encoding="utf-8")
    assert src.count("\n# ") >= 5, "fixture no longer uses level-1 sections"
    findings = check(src, DE_POL.read_text(encoding="utf-8"), lang="de")
    heading_findings = [f for f in findings if "headings" in f.detail]
    assert not heading_findings, [str(f) for f in heading_findings]
