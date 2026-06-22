from urllib.parse import urlencode
from uuid import uuid4

from fastapi import HTTPException, status

from src.core.config import get_settings
from src.schemas.auth import AuthTokens
from src.services.auth_service import AuthService
from src.utils.enums import RoleEnum


class GoogleOAuthService:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def get_authorization_url(self) -> str:
        settings = get_settings()
        params = {
            "client_id": settings.google_client_id or "TODO_GOOGLE_CLIENT_ID",
            "redirect_uri": settings.google_redirect_uri,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent",
        }
        return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

    def exchange_code(self, code: str) -> AuthTokens:
        settings = get_settings()
        if settings.allow_mock_google_oauth:
            return self.auth_service.issue_tokens(
                user_id=f"mock-google-{uuid4()}",
                email="admin@himtrek.local",
                name="Mock Admin",
                role=RoleEnum.admin,
            )

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="TODO: configure Google OAuth client credentials and token exchange flow",
        )
