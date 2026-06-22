from fastapi import APIRouter, Depends

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.inquiry import InquiryRecord, InquiryStatusUpdate
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/inquiries")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[InquiryRecord]], dependencies=[admin_guard])
def list_inquiries():
    return {"items": get_registry().inquiry_service.list_inquiries()}


@router.patch("/{inquiry_id}", response_model=InquiryRecord, dependencies=[admin_guard])
def update_inquiry_status(inquiry_id: str, payload: InquiryStatusUpdate):
    updated = get_registry().inquiry_service.update_status(inquiry_id, payload)
    if updated is None:
        raise NotFoundError("Inquiry not found")
    return updated
