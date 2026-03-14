# Import all models so they register with Base.metadata.
# This ensures relationships using string references resolve correctly.

from src.domain.users import User, Session  # noqa: F401
from src.domain.frameworks import (  # noqa: F401
    Framework,
    FrameworkControl,
    CrossFrameworkMapping,
)
from src.domain.control_groups import ControlGroup, control_group_controls  # noqa: F401
from src.domain.content import Policy, Requirement, Implementation  # noqa: F401
from src.domain.assessments import (  # noqa: F401
    Assessment,
    AssessmentSheet,
    AssessmentItem,
)
from src.domain.compliance import Evidence, Gap  # noqa: F401
from src.domain.qa import CorrelationResult  # noqa: F401
from src.domain.system import AuditLog, DataLoadHistory  # noqa: F401
