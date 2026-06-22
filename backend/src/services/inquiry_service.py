import logging

from src.repositories.inquiry_repository import InquiryRepository
from src.schemas.inquiry import (
    ContactInquiryCreate,
    CorporateInquiryCreate,
    InquiryCreatedResponse,
    InquiryRecord,
    InquiryStatusUpdate,
    TrekInquiryCreate,
)
from src.utils.enums import InquiryStatusEnum, InquiryTypeEnum

logger = logging.getLogger(__name__)


class InquiryService:
    def __init__(self, repository: InquiryRepository):
        self.repository = repository

    def list_inquiries(self) -> list[InquiryRecord]:
        return self.repository.list()

    def create_trek_inquiry(self, payload: TrekInquiryCreate) -> InquiryCreatedResponse:
        record = self.repository.create(
            InquiryRecord,
            {
                "type": InquiryTypeEnum.trek,
                "status": InquiryStatusEnum.received,
                "name": payload.name,
                "email": payload.email,
                "phone": payload.phone,
                "trek_id": payload.trek_id,
                "departure_id": payload.departure_id,
                "message": payload.message,
                "source": payload.source,
            },
        )
        logger.info("TODO: implement notification provider for trek inquiry %s", record.id)
        return InquiryCreatedResponse(id=record.id, status=record.status, message="Inquiry submitted successfully")

    def create_corporate_inquiry(self, payload: CorporateInquiryCreate) -> InquiryCreatedResponse:
        record = self.repository.create(
            InquiryRecord,
            {
                "type": InquiryTypeEnum.corporate,
                "status": InquiryStatusEnum.received,
                "company_name": payload.company_name,
                "contact_name": payload.contact_name,
                "email": payload.email,
                "phone": payload.phone,
                "team_size": payload.team_size,
                "preferred_month": payload.preferred_month,
                "message": payload.message,
                "source": payload.source,
            },
        )
        logger.info("TODO: implement notification provider for corporate inquiry %s", record.id)
        return InquiryCreatedResponse(id=record.id, status=record.status, message="Corporate inquiry submitted successfully")

    def create_contact_inquiry(self, payload: ContactInquiryCreate) -> InquiryCreatedResponse:
        record = self.repository.create(
            InquiryRecord,
            {
                "type": InquiryTypeEnum.contact,
                "status": InquiryStatusEnum.received,
                "name": payload.name,
                "email": payload.email,
                "phone": payload.phone,
                "message": payload.message,
                "source": payload.source,
            },
        )
        logger.info("TODO: implement notification provider for general contact inquiry %s", record.id)
        return InquiryCreatedResponse(id=record.id, status=record.status, message="Contact inquiry submitted successfully")

    def update_status(self, inquiry_id: str, payload: InquiryStatusUpdate) -> InquiryRecord | None:
        return self.repository.update(inquiry_id, payload.model_dump())
