from fastapi import APIRouter, Depends

from src.core.deps import require_roles
from src.schemas.landing_page import LandingPageContentUpdate, LandingPageResponse
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/content")
admin_guard = Depends(require_roles(RoleEnum.admin, RoleEnum.editor))


@router.get("/landing-page", response_model=LandingPageResponse, dependencies=[admin_guard])
def get_admin_landing_page():
    return get_registry().content_service.get_landing_page()


@router.patch("/landing-page", response_model=LandingPageResponse, dependencies=[admin_guard])
def update_landing_page(payload: LandingPageContentUpdate):
    return get_registry().content_service.update_landing_page(payload)
