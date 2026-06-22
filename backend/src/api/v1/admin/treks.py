from fastapi import APIRouter, Depends, status

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.trek import TrekCreate, TrekListItem, TrekUpdate
from src.utils.enums import RoleEnum
from src.services.service_registry import get_registry

router = APIRouter(prefix="/admin/treks")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[TrekListItem]], dependencies=[admin_guard])
def list_admin_treks():
    return {"items": get_registry().trek_repository.list()}


@router.post("", response_model=TrekListItem, status_code=status.HTTP_201_CREATED, dependencies=[admin_guard])
def create_trek(payload: TrekCreate):
    return get_registry().trek_repository.create_trek(payload)


@router.patch("/{trek_id}", response_model=TrekListItem, dependencies=[admin_guard])
def update_trek(trek_id: str, payload: TrekUpdate):
    updated = get_registry().trek_repository.update_trek(trek_id, payload)
    if updated is None:
        raise NotFoundError("Trek not found")
    return updated


@router.delete("/{trek_id}", response_model=dict[str, bool], dependencies=[admin_guard])
def delete_trek(trek_id: str):
    deleted = get_registry().trek_repository.delete(trek_id)
    if not deleted:
        raise NotFoundError("Trek not found")
    return {"deleted": True}
