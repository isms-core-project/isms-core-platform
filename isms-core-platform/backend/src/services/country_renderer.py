"""
country_renderer.py — Phase 22 country-aware POL token renderer.

Loads per-country YAML configs and applies token substitutions to policy
content at render time, so CH source POLs are served with the correct
regulatory references for each tenant's country.

Usage:
    content = country_renderer.render(raw_content, "fr")
    content = country_renderer.render(raw_content, None)   # returns unchanged
"""

import logging
from functools import lru_cache
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

_CONFIGS_DIR = Path(__file__).parent / "country_configs"
_CH_CODE = "ch"  # Switzerland — no substitution applied


@lru_cache(maxsize=None)
def _load_config(country_code: str) -> list[tuple[str, str]]:
    """
    Load and cache token substitution list for a country code.
    Returns pairs sorted longest-first to prevent partial matches.
    Raises FileNotFoundError if the config does not exist.
    """
    path = _CONFIGS_DIR / f"{country_code.lower()}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No country config for '{country_code}' at {path}")
    with open(path, encoding="utf-8") as fh:
        config = yaml.safe_load(fh)
    tokens: dict = config.get("tokens", {})
    return sorted(tokens.items(), key=lambda kv: len(kv[0]), reverse=True)


def render(content: str, country_code: str | None) -> str:
    """
    Apply country token substitutions to content.

    - If country_code is None or 'ch', returns content unchanged.
    - If the config is missing, logs a warning and returns content unchanged.
    """
    if not country_code or country_code.lower() == _CH_CODE:
        return content

    try:
        subs = _load_config(country_code.lower())
    except FileNotFoundError:
        logger.warning("country_renderer: no config for country '%s' — serving CH content", country_code)
        return content

    for old, new in subs:
        content = content.replace(old, new)

    return content


def available_countries() -> list[str]:
    """Return sorted list of supported country codes (from bundled YAML files)."""
    return sorted(p.stem for p in _CONFIGS_DIR.glob("*.yaml"))
