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

ZH_SMALL = """<!-- ISMS-CORE:POLICY:ISMS-OP-POL-T.1-ZH-HANT:operational:OP-POL:t.1 -->
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
    assert "## headings" in " ".join(str(f) for f in findings)


def test_line_delta_tolerance():
    plus_one = ZH_SMALL.replace("## 目的\n", "## 目的\n\n")
    assert "structure" not in gates(check(EN_SMALL, plus_one, lang="zh-Hant"))
    plus_three = ZH_SMALL.replace("## 目的\n", "## 目的\n\n\n\n")
    assert "structure" in gates(check(EN_SMALL, plus_three, lang="zh-Hant"))


def test_wrong_watermark_suffix_is_caught():
    broken = ZH_SMALL.replace("ISMS-OP-POL-T.1-ZH-HANT:", "ISMS-OP-POL-T.1-ZH:")
    findings = check(EN_SMALL, broken, lang="zh-Hant")
    assert "identifier" in gates(findings)


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
