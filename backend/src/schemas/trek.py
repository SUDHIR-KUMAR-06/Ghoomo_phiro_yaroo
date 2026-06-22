from pydantic import BaseModel, Field

from src.schemas.common import BaseDocument
from src.utils.enums import ContentStatusEnum, DifficultyEnum


class TrekBase(BaseModel):
    name: str
    slug: str
    badge: str
    duration_days: int = Field(gt=0)
    altitude_ft: int = Field(gt=0)
    difficulty: DifficultyEnum
    region: str
    batch_year: int = Field(ge=2024)
    summary: str
    description: str | None = None
    is_featured: bool = False
    hero_image_id: str | None = None
    hero_image_url: str | None = None
    status: ContentStatusEnum = ContentStatusEnum.published


class TrekCreate(TrekBase):
    pass


class TrekUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    badge: str | None = None
    duration_days: int | None = None
    altitude_ft: int | None = None
    difficulty: DifficultyEnum | None = None
    region: str | None = None
    batch_year: int | None = None
    summary: str | None = None
    description: str | None = None
    is_featured: bool | None = None
    hero_image_id: str | None = None
    hero_image_url: str | None = None
    status: ContentStatusEnum | None = None


class TrekSummary(TrekBase, BaseDocument):
    pass


class TrekListItem(BaseDocument):
    name: str
    slug: str
    badge: str
    duration_days: int
    altitude_ft: int
    difficulty: DifficultyEnum
    region: str
    batch_year: int
    summary: str
    hero_image: str | None = None
    is_featured: bool
