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

# The character sets live in their own module because the document gate
# (localization/zh_check.py) needs the same facts. See charsets.py for why the
# sets are validated against OpenCC rather than trusted as typed.
from charsets import SIMPLIFIED_ONLY, TRADITIONAL_ONLY, cjk  # noqa: E402


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
    hant_seen: dict[str, tuple[int, str]] = {}

    counts: dict[str, int] = {}
    for e in entries:
        if isinstance(e.get("en"), str):
            counts[e["en"].strip().lower()] = counts.get(e["en"].strip().lower(), 0) + 1
    shared_en = {k for k, n in counts.items() if n > 1}

    for i, e in enumerate(entries):
        where = f"entry[{i}] {e.get('en', '?')!r}"

        for field in ("en", "hant", "hans", "kind"):
            if not isinstance(e.get(field), str) or not e.get(field):
                errors.append(f"{where}: missing or empty {field!r}")
        if errors and errors[-1].startswith(where):
            continue

        # The derivation pass substitutes these literally; a newline inside a
        # term would change the file's line count.
        for field in ("en", "hant", "hans"):
            if "\n" in e[field]:
                errors.append(f"{where}: {field} contains a newline")

        if e["kind"] not in VALID_KINDS:
            errors.append(f"{where}: kind {e['kind']!r} not in {sorted(VALID_KINDS)}")

        key = (e["en"].strip().lower(), e["kind"])
        if key in seen:
            errors.append(
                f"{where}: duplicate of entry[{seen[key]}] (same term and kind)"
            )
        seen[key] = i

        # Same hant key, different hans: the dangerous one. Derivation builds a
        # dict keyed on hant, so the later entry silently wins and the earlier
        # one becomes dead text — no error, just a different translation of
        # whichever documents happen to hit it. Two entries sharing a hant key
        # *and* a hans are fine and intentional (Workflow and process are both
        # 流程 in this corpus), which is why the check is on the pair.
        prior = hant_seen.get(e["hant"].strip())
        if prior is not None and prior[1] != e["hans"].strip():
            errors.append(
                f"{where}: hant {e['hant']!r} already maps to {prior[1]!r} "
                f"at entry[{prior[0]}], but this entry says {e['hans']!r}"
            )
        hant_seen.setdefault(e["hant"].strip(), (i, e["hans"].strip()))

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

        # The same English surface form may carry two senses ('Classification'
        # as a Document Control label is 機密等級/密级; as a term it is
        # 分類/分类). That is legitimate, but the distinction has to be
        # readable from the data: an entry sharing its `en` with another must
        # say why it is separate. Reading the two columns alone cannot tell a
        # deliberate split from a stale duplicate, and anything a reader has
        # to infer from a source comment will eventually be inferred wrongly.
        if e["en"].strip().lower() in shared_en:
            if not (e.get("note") or e.get("variant_note")):
                errors.append(
                    f"{where}: shares its English form with another entry but "
                    f"has no note explaining how the two differ"
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
