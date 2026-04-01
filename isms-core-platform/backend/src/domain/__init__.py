# Import all models so they register with Base.metadata.
# This ensures relationships using string references resolve correctly.
# Organisation must be first — User/Project/Connector all reference it by string.

from src.domain.organisations import Organisation  # noqa: F401
from src.domain.users import User, Session  # noqa: F401
from src.domain.frameworks import (  # noqa: F401
    Framework,
    FrameworkControl,
    CrossFrameworkMapping,
)
from src.domain.control_groups import ControlGroup, control_group_controls  # noqa: F401
from src.domain.content import Policy, Requirement, Implementation  # noqa: F401
# Projects must be registered before any model that holds a project_id FK
from src.domain.projects import (  # noqa: F401
    Project,
    ProjectPolicy,
    ProjectImplementation,
    ProjectChecklist,
)
from src.domain.assessments import (  # noqa: F401
    Assessment,
    AssessmentSheet,
    AssessmentItem,
)
from src.domain.connectors import Connector, ConnectorEvidence  # noqa: F401
from src.domain.compliance import Evidence, Gap  # noqa: F401
from src.domain.qa import CorrelationResult  # noqa: F401
from src.domain.system import AuditLog, DataLoadHistory  # noqa: F401
from src.domain.collections import AssessmentCollection, collection_assessments  # noqa: F401
from src.domain.csrm import CsrmAssessment, CsrmBaselineRating, CsrmElevatedTom, CsrmProtectionObject  # noqa: F401
