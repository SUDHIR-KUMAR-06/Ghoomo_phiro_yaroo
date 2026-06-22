from fastapi import APIRouter, Depends, status

from src.core.deps import require_roles
from src.core.exceptions import NotFoundError
from src.schemas.media import MediaAsset, MediaAssetCreate
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/media")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("", response_model=dict[str, list[MediaAsset]], dependencies=[admin_guard])
def list_media():
    return {"items": get_registry().media_service.list_media()}


@router.post("/upload", response_model=MediaAsset, status_code=status.HTTP_201_CREATED, dependencies=[admin_guard])
def upload_media(payload: MediaAssetCreate):
    return get_registry().media_service.create_media(payload)


@router.delete("/{media_id}", response_model=dict[str, bool], dependencies=[admin_guard])
def delete_media(media_id: str):
    deleted = get_registry().media_service.delete_media(media_id)
    if not deleted:
        raise NotFoundError("Media asset not found")
    return {"deleted": True}
