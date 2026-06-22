from fastapi import APIRouter

from src.schemas.faq import FAQItem
from src.services.service_registry import get_registry

router = APIRouter(prefix="/faqs")


@router.get("", response_model=dict[str, list[FAQItem]])
def list_faqs():
    return {"items": get_registry().content_service.get_faqs()}
