from pydantic import BaseModel


class SiteSettingResponse(BaseModel):
    contact_email: str
    contact_phone: str
    contact_locations: list[str]
    google_oauth_enabled: bool
    use_mock_db: bool
