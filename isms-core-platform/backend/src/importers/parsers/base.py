"""Base classes for policy file parsers."""

import hashlib
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Section:
    """A heading + body pair from a parsed document."""

    heading: str
    body: str
    level: int  # heading level (1-4)


@dataclass
class ParsedPolicy:
    """Intermediate representation of a parsed policy file."""

    document_id: str  # e.g. "ISMS-POL-A.5.24-28" or "ISMS-OP-POL-A.5.24-28"
    title: str
    product_type: str  # "framework", "operational", or "external"
    policy_type: str  # "POL", "OP-POL", "INS", "REF", "CTX", "FORM"
    group_code: str  # e.g. "a.5.24-28"
    content_hash: str  # SHA-256 of raw file bytes
    word_count: int
    sections: list[Section] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    language: str = "en"          # ISO 639-1: en, de, fr, it
    source_label: str | None = None  # External docs only: "Acme Corp", "Previous consultant"


# Regex to extract control reference from document ID
# Matches: ISMS-POL-A.5.24-28, ISMS-OP-POL-A.8.24, ISMS-REF-A.8.15,
#          ISMS-CTX-A.8.28, ISMS-FORM-A.8.10-GDPR, ISMS-POL-A.5.1-2-6.1-2
#          ISMS-INS-POL-00, ISMS-INS-POL-01
_DOC_ID_PATTERN = re.compile(
    r"ISMS-(?:OP-)?(?:INS-)?(?:POL|REF|CTX|FORM|IMP)-([A-Za-z0-9][\w.\-]+)"
)

# Foundation policy prefixes — map to group_code "00"
_FOUNDATION_PREFIX_RE = re.compile(
    r"^ISMS-(?:INS-POL|POL)-0[01]\b", re.IGNORECASE
)


def derive_group_code(document_id: str) -> str:
    """Extract group_code from a document ID.

    ISMS-POL-A.5.24-28      → a.5.24-28
    ISMS-OP-POL-A.8.24      → a.8.24
    ISMS-INS-POL-00-...     → 00  (foundation)
    ISMS-POL-00-...         → 00  (foundation)
    ISMS-REF-DORA-...       → dora (non-ISO ref, maps to foundation group)
    """
    # Foundation policies (POL-00, POL-01, INS-POL-00, INS-POL-01)
    if _FOUNDATION_PREFIX_RE.match(document_id):
        return "00"

    m = _DOC_ID_PATTERN.search(document_id)
    if m:
        return m.group(1).lower()
    raise ValueError(f"Cannot extract group_code from document_id: {document_id}")


def detect_product_and_type(document_id: str) -> tuple[str, str]:
    """Detect product_type and document_type from document ID prefix.

    ISMS-OP-POL-*  → ("operational", "OP-POL")
    ISMS-INS-*     → ("framework",  "INS")
    ISMS-POL-*     → ("framework",  "POL")
    ISMS-IMP-*     → ("framework",  "IMP")
    ISMS-REF-*     → ("framework",  "REF")
    ISMS-CTX-*     → ("framework",  "CTX")
    ISMS-FORM-*    → ("framework",  "FORM")
    """
    upper = document_id.upper()
    if "ISMS-OP-POL-" in upper:
        return "operational", "OP-POL"
    if "ISMS-INS-" in upper:
        return "framework", "INS"
    if "ISMS-IMP-" in upper:
        return "framework", "IMP"
    if "ISMS-REF-" in upper:
        return "framework", "REF"
    if "ISMS-CTX-" in upper:
        return "framework", "CTX"
    if "ISMS-FORM-" in upper:
        return "framework", "FORM"
    return "framework", "POL"


# IMP UG/TG suffix pattern
_IMPL_TYPE_RE = re.compile(r"-(UG|TG)\b")


def detect_impl_type(document_id: str) -> str:
    """Extract UG or TG from an IMP document ID.

    ISMS-IMP-A.5.24-28.S1-UG → "UG"
    ISMS-IMP-A.5.24-28.S1-TG → "TG"
    ISMS-IMP-A.8.8.12-P3     → "TG" (unsplit P3/P4 are continuation TG)
    """
    m = _IMPL_TYPE_RE.search(document_id)
    return m.group(1).upper() if m else "TG"


def compute_content_hash(file_path: Path) -> str:
    """SHA-256 hash of raw file bytes."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


class BasePolicyParser(ABC):
    """Abstract base class for policy file parsers."""

    @abstractmethod
    def parse(self, file_path: Path) -> ParsedPolicy:
        """Parse a policy file and return a ParsedPolicy."""
        ...

    @abstractmethod
    def supported_extensions(self) -> list[str]:
        """Return list of supported file extensions (e.g. ['.md'])."""
        ...
