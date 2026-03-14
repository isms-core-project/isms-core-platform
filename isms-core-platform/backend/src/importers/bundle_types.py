import enum


class BundleType(str, enum.Enum):
    SINGLE_FRAMEWORK = "single_framework"
    MULTI_FRAMEWORK = "multi_framework"
    CONTROL_GROUPS = "control_groups"
    CROSSWALK = "crosswalk"


def detect_bundle_type(data: dict) -> BundleType | None:
    """Determine bundle type from top-level keys and first object type."""
    if "frameworks" in data and isinstance(data["frameworks"], list):
        return BundleType.MULTI_FRAMEWORK
    if "framework" in data and isinstance(data["framework"], dict):
        return BundleType.SINGLE_FRAMEWORK
    if "dataset" in data and "objects" in data:
        objects = data.get("objects", [])
        if objects:
            obj_type = objects[0].get("type")
            if obj_type == "control_group":
                return BundleType.CONTROL_GROUPS
            if obj_type == "cross_framework_mapping":
                return BundleType.CROSSWALK
    return None
