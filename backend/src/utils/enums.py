from enum import Enum


class RoleEnum(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"


class DifficultyEnum(str, Enum):
    easy = "easy"
    moderate = "moderate"
    moderate_plus = "moderate+"
    challenging = "challenging"


class DepartureStatusEnum(str, Enum):
    scheduled = "scheduled"
    full = "full"
    cancelled = "cancelled"
    completed = "completed"


class InquiryTypeEnum(str, Enum):
    trek = "trek"
    corporate = "corporate"
    contact = "contact"


class InquiryStatusEnum(str, Enum):
    received = "received"
    contacted = "contacted"
    converted = "converted"
    closed = "closed"


class ContentStatusEnum(str, Enum):
    draft = "draft"
    published = "published"
