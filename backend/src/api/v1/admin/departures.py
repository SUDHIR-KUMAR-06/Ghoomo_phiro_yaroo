from fastapi import APIRouter, Depends, status

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.departure import Departure, DepartureCreate, DepartureUpdate
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/departures")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[Departure]], dependencies=[admin_guard])
def list_admin_departures():
    return {"items": get_registry().departure_repository.list()}


@router.post("", response_model=Departure, status_code=status.HTTP_201_CREATED, dependencies=[admin_guard])
def create_departure(payload: DepartureCreate):
    return get_registry().departure_repository.create_departure(payload)


@router.patch("/{departure_id}", response_model=Departure, dependencies=[admin_guard])
def update_departure(departure_id: str, payload: DepartureUpdate):
    updated = get_registry().departure_repository.update_departure(departure_id, payload)
    if updated is None:
        raise NotFoundError("Departure not found")
    return updated


@router.delete("/{departure_id}", response_model=dict[str, bool], dependencies=[admin_guard])
def delete_departure(departure_id: str):
    deleted = get_registry().departure_repository.delete(departure_id)
    if not deleted:
        raise NotFoundError("Departure not found")
    return {"deleted": True}
