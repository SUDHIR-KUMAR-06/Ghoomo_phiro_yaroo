from fastapi import APIRouter, Depends, status

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.testimonial import TestimonialCreate, TestimonialItem, TestimonialUpdate
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/testimonials")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[TestimonialItem]], dependencies=[admin_guard])
def list_admin_testimonials():
    return {"items": get_registry().testimonial_repository.list()}


@router.post("", response_model=TestimonialItem, status_code=status.HTTP_201_CREATED, dependencies=[admin_guard])
def create_testimonial(payload: TestimonialCreate):
    return get_registry().testimonial_repository.create_testimonial(payload)


@router.patch("/{testimonial_id}", response_model=TestimonialItem, dependencies=[admin_guard])
def update_testimonial(testimonial_id: str, payload: TestimonialUpdate):
    updated = get_registry().testimonial_repository.update_testimonial(testimonial_id, payload)
    if updated is None:
        raise NotFoundError("Testimonial not found")
    return updated


@router.delete("/{testimonial_id}", response_model=dict[str, bool], dependencies=[admin_guard])
def delete_testimonial(testimonial_id: str):
    deleted = get_registry().testimonial_repository.delete(testimonial_id)
    if not deleted:
        raise NotFoundError("Testimonial not found")
    return {"deleted": True}
