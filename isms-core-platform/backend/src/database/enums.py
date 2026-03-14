import enum


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    ISMS_MANAGER = "isms_manager"
    AUDITOR = "auditor"
    CONTROL_OWNER = "control_owner"
    VIEWER = "viewer"


class ProductType(str, enum.Enum):
    FRAMEWORK = "framework"
    OPERATIONAL = "operational"
    EXTERNAL = "external"
    PRIVACY = "privacy"
    CLOUD = "cloud"


class PrivacyRole(str, enum.Enum):
    CONTROLLER = "CONTROLLER"
    PROCESSOR = "PROCESSOR"
    BOTH = "BOTH"


class ProductFamily(str, enum.Enum):
    ISMS = "ISMS"
    PRIVACY = "PRIVACY"
    CLOUD = "CLOUD"


class PolicyType(str, enum.Enum):
    POL = "POL"
    OP_POL = "OP-POL"
    INS = "INS"
    REF = "REF"
    CTX = "CTX"
    FORM = "FORM"


class ImplType(str, enum.Enum):
    UG = "UG"
    TG = "TG"


class ComplianceStatus(str, enum.Enum):
    COMPLIANT = "compliant"
    PARTIAL = "partial"
    NON_COMPLIANT = "non_compliant"
    NOT_ASSESSED = "not_assessed"
    NA = "na"


class GapSeverity(str, enum.Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class GapStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"
    ACCEPTED = "accepted"


class AssessmentType(str, enum.Enum):
    DETAILED = "detailed"
    CHECKLIST = "checklist"


class SheetType(str, enum.Enum):
    EXECUTIVE_SUMMARY = "executive_summary"
    DASHBOARD = "dashboard"
    ASSESSMENT = "assessment"
    REFERENCE = "reference"
    CONFIG = "config"


class EvidenceType(str, enum.Enum):
    DOCUMENT = "document"
    SCREENSHOT = "screenshot"
    LOG_EXTRACT = "log_extract"
    CONFIG_EXPORT = "config_export"
    TEST_RESULT = "test_result"
    ATTESTATION = "attestation"


class EvidenceStatus(str, enum.Enum):
    DRAFT = "draft"                   # Uploaded, not yet assigned to a control
    PENDING_REVIEW = "pending_review" # Assigned, awaiting manager approval
    APPROVED = "approved"             # Approved by admin/isms_manager
    REJECTED = "rejected"             # Rejected — needs rework
    ACTIVE = "active"                 # Assigned, no approval required


class MappingType(str, enum.Enum):
    MAPS_TO = "maps-to"
    PARTIALLY_MAPS_TO = "partially-maps-to"
    RELATED_TO = "related-to"
    MITIGATES = "mitigates"
    DETECTS = "detects"
    SUPPORTS = "supports"
    DEPENDS_ON = "depends-on"
    ENABLES = "enables"
    FEEDS_INTO = "feeds-into"
    IMPLEMENTS = "implements"


class CorrelationMethod(str, enum.Enum):
    EXISTENCE = "existence"
    KEYWORD = "keyword"
    SEMANTIC = "semantic"           # sentence-transformers (mini LLM, CPU)
    SEMANTIC_CLAUDE = "semantic_claude"  # Anthropic Claude API
    MANUAL = "manual"


class QAStatus(str, enum.Enum):
    PASS = "pass"
    WARNING = "warning"
    FAIL = "fail"
    NEEDS_REVIEW = "needs_review"


class ControlGroupStatus(str, enum.Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    BASIC = "basic"
    INCOMPLETE = "incomplete"


class GovernanceMode(str, enum.Enum):
    PLATFORM = "platform"   # DB is master — edit in WebUI, publish to MD
    LOCAL = "local"         # Files are master — import triggers DB sync


class ContentState(str, enum.Enum):
    DRAFT = "draft"         # Work in progress — not visible to read-only users
    REVIEW = "review"       # Submitted for peer/manager review
    APPROVED = "approved"   # Approved — ready to publish
    PUBLISHED = "published" # Live — visible to all authenticated users


class EditSource(str, enum.Enum):
    IMPORT = "import"   # Change came from the file import pipeline
    WEBUI = "webui"     # Change made via the platform WebUI
    API = "api"         # Change made via direct API call (non-WebUI client)
