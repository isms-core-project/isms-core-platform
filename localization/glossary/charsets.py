#!/usr/bin/env python3
"""Script-specific character sets, shared by the termbase lint and the gate.

One list of facts, two consumers:

* ``lint_termbase`` uses them to catch a Simplified character pasted into the
  Traditional column of a glossary entry (or the reverse).
* ``zh_check`` uses them to catch the same leak in a whole translated document
  — the mistake is easy to make by hand and invisible when skimming, because
  a single wrong glyph in 150 lines reads as normal Chinese.

Neither set is trusted as typed. ``check_against_opencc`` fails any character
OpenCC does not actually convert the way the set claims, because hand-typed
character lists quietly accumulate errors: 事 and 它 were both wrongly listed
here at first and would have flagged correct Traditional text as broken, and
周 was found the first time that check ran. OpenCC does not lie about them.

The two sets are deliberately asymmetric. 週 is never Simplified, but 周 is
correct Traditional (周圍, 周詳) *and* the Simplified form of 週 — so 週 belongs
to the Traditional-only set while 周 belongs to neither. Forcing the sets to
mirror would put 周 back and hand correct Traditional text a false positive.

A character whose script depends on the word rather than the glyph may not go
in either set; those live in KNOWN_SHARED with their reasoning.
"""

from __future__ import annotations

# Characters that exist only in Simplified Chinese. None may appear in hant.
SIMPLIFIED_ONLY = set(
    "网络据软应权审记录风险评训练认识营运产场结构户账问访远动设实体确档标级态历变"
    "质证范围键点执讯资简单复备库览报径联义项适声沟类条规隐础码镜华员层务护严开阅机"
    "与关后说们为谁么盖图称价业赖预头顶构则续频见没书让从内义气"
    "测试验读写储传输费转达违该个会区难进过还这对时题样种统线织习学"
    "发现单双万无长门电车东马鸟龙宝岁帅师归当录总举办尽汇"
)

# Characters that exist only in Traditional Chinese. None may appear in hans.
TRADITIONAL_ONLY = set(
    "網絡據軟應權審記錄風險評訓練認識營運產場結構戶帳問訪遠動設實體確檔標級態歷變週"
    "質證範圍鍵點執訊資簡單復備庫覽報徑聯義項適聲溝類條規隱礎碼鏡華員層務護嚴開閱機"
    "與關後說們為誰麼蓋圖稱價業賴預頭頂構則續頻見沒書讓從內義氣"
    "測試驗讀寫儲傳輸費轉達違該個會區難進過還這對時題樣種統線織習學"
    "發現單雙萬無長門電車東馬鳥龍寶歲帥師歸當錄總舉辦盡匯"
)

# Characters OpenCC rewrites but that are legitimate in BOTH scripts, so
# neither set may claim them. Kept explicit with the reason, because the
# automated gap-finder below subtracts this list and would otherwise report
# them forever:
#   准  核准 (T)          vs 准許 (S)         — word-dependent merge
#   台  平台 (T)          vs 台湾 (S)         — 臺/台 both Traditional
#   只  只是 (both)                            — word-dependent merge
#   干  干預 (T)          vs 干 (S, of 乾/幹)
#   云  詩云 (T)          vs 云 (S, of 雲)    — word-dependent merge
#   于  于 (T, surname)   vs 于 (S, of 於)
#   里  公里 (T)          vs 里 (S, of 裡/裏)
#   松  松樹 (T)          vs 松 (S, of 鬆)
#   划  划船 (T)          vs 划 (S, of 劃)
#   采  采風 (T)          vs 采 (S, of 採)
#   系  系統 (T)          vs 系 (S, of 係/繫)
#   制  控制 (T)          vs 制 (S, of 製)
#   面  方面 (T)          vs 面 (S, of 麵)
KNOWN_SHARED = set("准台只干云于里松划采系制面")

# 后 is deliberately absent from KNOWN_SHARED despite 皇后 being legitimate
# Traditional: in governance prose it is overwhelmingly the Simplified form of
# 後, and the false positive needs the word 皇后 specifically. Revisit if this
# corpus ever grows a document where it would fire.

# Which set a language may NOT contain, keyed by every tag spelling in use.
#
# Two tag conventions are live in this repo: the termbase declares zh-TW/zh-CN
# as primary with zh-Hant/zh-Hans as alternatives, and zh_check's CLI defaults
# to zh-Hant. A table keyed on one spelling only would leave this gate silently
# disabled for every caller using the other — no error, just no check.
TRADITIONAL_TAGS = ("zh-tw", "zh-hant", "zh-hk", "zh-mo")
SIMPLIFIED_TAGS = ("zh-cn", "zh-hans", "zh-sg")

FORBIDDEN: dict[str, set[str]] = {}
for _tag in TRADITIONAL_TAGS:
    FORBIDDEN[_tag] = SIMPLIFIED_ONLY
for _tag in SIMPLIFIED_TAGS:
    FORBIDDEN[_tag] = TRADITIONAL_ONLY
del _tag
SCRIPT_NAME = {id(SIMPLIFIED_ONLY): "Simplified", id(TRADITIONAL_ONLY): "Traditional"}


def normalise(lang: str) -> str:
    return lang.lower().replace("_", "-")


def leak_candidates(text: str, lang: str, cc_s2t, cc_t2s) -> set[str]:
    """Characters in `text` that look like the other script, given `lang`.

    The test is necessary but not sufficient: a character qualifies when OpenCC
    gives it a distinct form in the other script and leaves it alone coming
    back. 准 and 台 pass that test and are still correct Traditional, which is
    why this cannot be the gate itself — it exists to *audit* the curated sets.
    Whatever it returns that is in neither set nor KNOWN_SHARED is a character
    the gate would silently wave through, i.e. a gap.

    Direction matters. Run on a Traditional document this finds Simplified
    characters, and on a Simplified document Traditional ones. Feeding a
    Simplified document through the Traditional direction reports every correct
    character it contains as a candidate — noise, not a finding.
    """
    tag = normalise(lang)
    if tag in TRADITIONAL_TAGS:
        outward, inward = cc_s2t, cc_t2s
    elif tag in SIMPLIFIED_TAGS:
        outward, inward = cc_t2s, cc_s2t
    else:
        return set()
    return {ch for ch in cjk(text)
            if outward.convert(ch) != ch and inward.convert(ch) == ch}


def uncovered(candidates: set[str], lang: str) -> set[str]:
    """Candidates the gate would miss: not covered, not known-shared."""
    forbidden = FORBIDDEN.get(normalise(lang))
    if forbidden is None:
        return set()
    return candidates - forbidden - KNOWN_SHARED


def cjk(text: str) -> str:
    """Keep only CJK ideographs — punctuation and Latin must not trip the check."""
    return "".join(ch for ch in text if "㐀" <= ch <= "鿿")


def leaks(text: str, lang: str) -> dict[str, list[int]]:
    """Chars from the wrong script, mapped to the 1-based lines they sit on.

    Line numbers matter: a bare list of characters is not actionable in a
    150-line document.
    """
    forbidden = FORBIDDEN.get(normalise(lang))
    if forbidden is None:
        return {}
    found: dict[str, list[int]] = {}
    for n, line in enumerate(text.splitlines(), 1):
        for ch in cjk(line):
            if ch in forbidden:
                found.setdefault(ch, []).append(n)
    return found


def check_against_opencc() -> list[str]:
    """Verify each character is genuinely script-specific, using OpenCC.

    A character listed as Simplified-only must carry a distinct Traditional
    form, i.e. OpenCC's s2t must change it. The mirror holds for the
    Traditional-only set with t2s. Anything else means the character is
    script-neutral or misspelled, and the entry is a false positive waiting to
    fail a correct document.

    The converters are built here rather than passed in: with two OpenCC
    handles in scope, calling them in the wrong order is silent and produces a
    uniformly wrong report (320 spurious findings the first time round).
    """
    try:
        import opencc
    except ImportError:  # pragma: no cover - environment dependent
        return []
    s2t, t2s = opencc.OpenCC("s2t"), opencc.OpenCC("t2s")

    problems: list[str] = []
    for chars, converter, other_script in (
        (SIMPLIFIED_ONLY, s2t, "Traditional"),
        (TRADITIONAL_ONLY, t2s, "Simplified"),
    ):
        for ch in sorted(chars):
            if converter.convert(ch) == ch:
                problems.append(
                    f"{ch!r} is listed as {other_script}-form but OpenCC "
                    f"converts it to itself — it is script-neutral or misspelled"
                )
    for ch in sorted(SIMPLIFIED_ONLY & TRADITIONAL_ONLY):
        problems.append(f"{ch!r} appears in both sets")
    overlap = KNOWN_SHARED & (SIMPLIFIED_ONLY | TRADITIONAL_ONLY)
    for ch in sorted(overlap):
        problems.append(f"{ch!r} is in KNOWN_SHARED and also in a script set")
    # No size check: the two sets are legitimately asymmetric. 週 is never
    # Simplified, but 周 is correct Traditional (周圍, 周詳) as well as the
    # Simplified form of 週 — so 週 is Traditional-only while 周 is neither.
    # The wording above ("none may appear in hant") is the whole contract; an
    # artificial mirror between the two sets would force 周 back in and hand
    # correct Traditional text a false positive.
    return problems
