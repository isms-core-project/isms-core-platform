#!/usr/bin/env python3
"""Lint the Chinese termbase.

The two columns are supposed to be different scripts of the same term. The
easy mistake is to leave the Traditional column half-converted (or paste a
Simplified string into it), which is invisible when skimming 200 rows but
obvious to a reader in Hong Kong. So the main check is character-set
membership: no Simplified-only character may appear in the hant column, and
no Traditional-only character in the hans column.

Entries whose two columns are legitimately identical (版本, 加密, 例外...)
must say so explicitly with "same": true. Silently identical rows are
rejected, which forces a deliberate decision rather than an oversight.

Usage:
    python3 localization/glossary/lint_termbase.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

TERMBASE = Path(__file__).with_name("zh-termbase.json")

VALID_KINDS = {"label", "heading", "term", "value"}

# Characters that exist only in Simplified Chinese. None may appear in hant.
SIMPLIFIED_ONLY = set(
    "网络据软应权审记录风险评训练认识营运产场结构户账问访远动设实体确档标级态历变周"
    "质证范围键点执讯资简单复备库览报径联义项适声沟类条规隐础码镜华员层务护严开阅机"
    "与关后说们为谁么盖图称价业赖预头顶构则续频见没书让从内义气"
    "测试验读写储传输费转达违该个会区难进过还这对时题样种统线织习学"
)
# Characters shared by both scripts are excluded on purpose (事, 它, 只...),
# as are the word-split merges 准/準 (核准 vs 標準) and 只/隻: neither set may
# contain a character whose script depends on the word rather than the glyph.
# The two sets below mirror each other one character at a time.

# Characters that exist only in Traditional Chinese. None may appear in hans.
TRADITIONAL_ONLY = set(
    "網絡據軟應權審記錄風險評訓練認識營運產場結構戶帳問訪遠動設實體確檔標級態歷變週"
    "質證範圍鍵點執訊資簡單復備庫覽報徑聯義項適聲溝類條規隱礎碼鏡華員層務護嚴開閱機"
    "與關後說們為誰麼蓋圖稱價業賴預頭頂構則續頻見沒書讓從內義氣"
    "測試驗讀寫儲傳輸費轉達違該個會區難進過還這對時題樣種統線織習學"
)


def cjk(text: str) -> str:
    return "".join(ch for ch in text if "㐀" <= ch <= "鿿")


def lint(termbase: dict) -> list[str]:
    errors: list[str] = []
    entries = termbase.get("entries")
    if not isinstance(entries, list) or not entries:
        return ["termbase has no entries"]

    keep = {k.lower() for k in termbase.get("keep_as_is", [])}
    # Keyed by (english, kind): the same surface form can carry two senses.
    # 'Classification' as a Document Control label is 機密等級/密级 (it holds
    # Internal / Confidential / Public); 'classification' as a term is
    # 分類/分类. Same word, different decision — both belong in the file.
    seen: dict[tuple[str, str], int] = {}

    for i, e in enumerate(entries):
        where = f"entry[{i}] {e.get('en', '?')!r}"

        for field in ("en", "hant", "hans", "kind"):
            if not isinstance(e.get(field), str) or not e.get(field):
                errors.append(f"{where}: missing or empty {field!r}")
        if errors and errors[-1].startswith(where):
            continue

        if e["kind"] not in VALID_KINDS:
            errors.append(f"{where}: kind {e['kind']!r} not in {sorted(VALID_KINDS)}")

        key = (e["en"].strip().lower(), e["kind"])
        if key in seen:
            errors.append(
                f"{where}: duplicate of entry[{seen[key]}] (same term and kind)"
            )
        seen[key] = i

        if e["en"].strip().lower() in keep:
            errors.append(f"{where}: also listed in keep_as_is")

        for col in ("hant", "hans"):
            if not cjk(e[col]):
                errors.append(f"{where}: {col} has no Chinese characters: {e[col]!r}")

        hit_s = sorted(set(cjk(e["hant"])) & SIMPLIFIED_ONLY)
        if hit_s:
            errors.append(
                f"{where}: Simplified characters in hant column: {''.join(hit_s)}"
                f" — hant={e['hant']!r}"
            )
        hit_t = sorted(set(cjk(e["hans"])) & TRADITIONAL_ONLY)
        if hit_t:
            errors.append(
                f"{where}: Traditional characters in hans column: {''.join(hit_t)}"
                f" — hans={e['hans']!r}"
            )

        identical = e["hant"] == e["hans"]
        if identical and not e.get("same"):
            errors.append(
                f"{where}: hant and hans are identical ({e['hant']!r}) "
                f"— set \"same\": true if intended"
            )
        if not identical and e.get("same"):
            errors.append(
                f"{where}: marked same:true but columns differ "
                f"({e['hant']!r} vs {e['hans']!r})"
            )

    return errors


def main() -> int:
    termbase = json.loads(TERMBASE.read_text(encoding="utf-8"))
    errors = lint(termbase)
    if errors:
        for err in errors:
            print(f"FAIL {err}")
        print(f"\n{len(errors)} problem(s)")
        return 1
    n = len(termbase["entries"])
    same = sum(1 for e in termbase["entries"] if e.get("same"))
    print(f"OK  {n} entries ({same} identical across scripts), "
          f"{len(termbase.get('keep_as_is', []))} keep-as-is")
    return 0


if __name__ == "__main__":
    sys.exit(main())
