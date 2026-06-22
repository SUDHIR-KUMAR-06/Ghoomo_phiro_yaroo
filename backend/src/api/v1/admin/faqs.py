from fastapi import APIRouter, Depends, status

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.faq import FAQCreate, FAQItem, FAQUpdate
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/faqs")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[FAQItem]], dependencies=[admin_guard])
def list_admin_faqs():
    return {"items": get_registry().faq_repository.list()}


@router.post("", response_model=FAQItem, status_code=status.HTTP_201_CREATED, dependencies=[admin_guard])
def create_faq(payload: FAQCreate):
    return get_registry().faq_repository.create_faq(payload)


@router.patch("/{faq_id}", response_model=FAQItem, dependencies=[admin_guard])
def update_faq(faq_id: str, payload: FAQUpdate):
    updated = get_registry().faq_repository.update_faq(faq_id, payload)
    if updated is None:
        raise NotFoundError("FAQ not found")
    return updated


@router.delete("/{faq_id}", response_model=dict[str, bool], dependencies=[admin_guard])
def delete_faq(faq_id: str):
    deleted = get_registry().faq_repository.delete(faq_id)
    if not deleted:
        raise NotFoundError("FAQ not found")
    return {"deleted": True}
