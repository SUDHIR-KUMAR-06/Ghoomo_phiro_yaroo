from fastapi import APIRouter

from src.core.config import get_settings
from src.schemas.setting import SiteSettingResponse
from src.services.service_registry import get_registry

router = APIRouter()


@router.get("/health")
def health_check():
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@router.get("/landing-page")
def get_landing_page():
    return get_registry().content_service.get_landing_page()


@router.get("/settings/public", response_model=SiteSettingResponse)
def get_public_settings() -> SiteSettingResponse:
    settings = get_settings()
    landing_page = get_registry().content_service.get_landing_page()
    return SiteSettingResponse(
        contact_email=landing_page.footer.contact_email,
        contact_phone=landing_page.footer.contact_phone,
        contact_locations=landing_page.footer.locations,
        google_oauth_enabled=bool(settings.google_client_id and settings.google_client_secret),
        use_mock_db=settings.use_mock_db,
    )
