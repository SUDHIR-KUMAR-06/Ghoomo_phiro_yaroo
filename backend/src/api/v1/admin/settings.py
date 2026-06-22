from fastapi import APIRouter, Depends

from src.core.config import get_settings
from src.core.deps import require_roles
from src.schemas.setting import SiteSettingResponse
from src.services.service_registry import get_registry
from src.utils.enums import RoleEnum

router = APIRouter(prefix="/admin/settings")
admin_guard = Depends(require_roles(RoleEnum.admin))


@router.get("", response_model=SiteSettingResponse, dependencies=[admin_guard])
def get_admin_settings():
    settings = get_settings()
    landing_page = get_registry().content_service.get_landing_page()
    return SiteSettingResponse(
        contact_email=landing_page.footer.contact_email,
        contact_phone=landing_page.footer.contact_phone,
        contact_locations=landing_page.footer.locations,
        google_oauth_enabled=bool(settings.google_client_id and settings.google_client_secret),
        use_mock_db=settings.use_mock_db,
    )
