from fastapi import APIRouter

from src.schemas.testimonial import TestimonialItem
from src.services.service_registry import get_registry

router = APIRouter(prefix="/testimonials")


@router.get("", response_model=dict[str, list[TestimonialItem]])
def list_testimonials():
    return {"items": get_registry().content_service.get_testimonials()}
