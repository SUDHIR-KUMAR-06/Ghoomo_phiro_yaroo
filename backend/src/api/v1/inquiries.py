from fastapi import APIRouter

from src.schemas.inquiry import (
    ContactInquiryCreate,
    CorporateInquiryCreate,
    InquiryCreatedResponse,
    TrekInquiryCreate,
)
from src.services.service_registry import get_registry

router = APIRouter(prefix="/inquiries")


@router.post("/trek", response_model=InquiryCreatedResponse, status_code=201)
def create_trek_inquiry(payload: TrekInquiryCreate):
    return get_registry().inquiry_service.create_trek_inquiry(payload)


@router.post("/corporate", response_model=InquiryCreatedResponse, status_code=201)
def create_corporate_inquiry(payload: CorporateInquiryCreate):
    return get_registry().inquiry_service.create_corporate_inquiry(payload)


@router.post("/contact", response_model=InquiryCreatedResponse, status_code=201)
def create_contact_inquiry(payload: ContactInquiryCreate):
    return get_registry().inquiry_service.create_contact_inquiry(payload)
