from fastapi import APIRouter, Query

from src.schemas.auth import AuthTokens, GoogleLoginResponse, LogoutRequest, RefreshTokenRequest
from src.schemas.common import APIMessage
from src.services.service_registry import get_registry

router = APIRouter(prefix="/auth")


@router.get("/google/login", response_model=GoogleLoginResponse)
def google_login():
    service = get_registry().google_oauth_service
    return GoogleLoginResponse(
        authorization_url=service.get_authorization_url(),
        message="TODO: configure Google OAuth credentials for production use.",
    )


@router.get("/google/callback", response_model=AuthTokens)
def google_callback(code: str = Query(..., description="OAuth authorization code")):
    return get_registry().google_oauth_service.exchange_code(code)


@router.post("/refresh", response_model=AuthTokens)
def refresh_tokens(payload: RefreshTokenRequest):
    return get_registry().auth_service.refresh_tokens(payload.refresh_token)


@router.post("/logout", response_model=APIMessage)
def logout(_: LogoutRequest):
    return APIMessage(message="TODO: persist refresh tokens if you want true server-side logout.")
