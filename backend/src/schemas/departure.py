from datetime import date

from pydantic import BaseModel, Field

from src.schemas.common import BaseDocument
from src.utils.enums import DepartureStatusEnum


class DepartureBase(BaseModel):
    trek_id: str
    trek_name: str
    departure_date: date
    month_label: str
    summary: str
    tags: list[str]
    seats_total: int | None = Field(default=None, ge=0)
    seats_available: int | None = Field(default=None, ge=0)
    status: DepartureStatusEnum = DepartureStatusEnum.scheduled


class DepartureCreate(DepartureBase):
    pass


class DepartureUpdate(BaseModel):
    trek_id: str | None = None
    trek_name: str | None = None
    departure_date: date | None = None
    month_label: str | None = None
    summary: str | None = None
    tags: list[str] | None = None
    seats_total: int | None = None
    seats_available: int | None = None
    status: DepartureStatusEnum | None = None


class Departure(BaseDocument, DepartureBase):
    pass
