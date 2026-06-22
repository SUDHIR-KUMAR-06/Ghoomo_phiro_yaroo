from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr, Field

from src.schemas.common import BaseDocument
from src.utils.enums import InquiryStatusEnum, InquiryTypeEnum


class InquiryBase(BaseModel):
    email: EmailStr
    phone: str = Field(min_length=8, max_length=20)
    message: str | None = None
    source: str


class TrekInquiryCreate(InquiryBase):
    name: str
    trek_id: str | None = None
    departure_id: str | None = None


class CorporateInquiryCreate(InquiryBase):
    company_name: str
    contact_name: str
    team_size: int | None = Field(default=None, ge=1)
    preferred_month: str | None = None


class ContactInquiryCreate(InquiryBase):
    name: str


class InquiryRecord(BaseDocument):
    type: InquiryTypeEnum
    status: InquiryStatusEnum = InquiryStatusEnum.received
    name: str | None = None
    company_name: str | None = None
    contact_name: str | None = None
    email: EmailStr
    phone: str
    trek_id: str | None = None
    departure_id: str | None = None
    team_size: int | None = None
    preferred_month: str | None = None
    message: str | None = None
    source: str
    submitted_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class InquiryStatusUpdate(BaseModel):
    status: InquiryStatusEnum


class InquiryCreatedResponse(BaseModel):
    id: str
    status: InquiryStatusEnum
    message: str
