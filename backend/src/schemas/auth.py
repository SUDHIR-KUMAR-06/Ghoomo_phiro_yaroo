from pydantic import BaseModel, EmailStr


class GoogleLoginResponse(BaseModel):
    authorization_url: str
    message: str


class TokenUser(BaseModel):
    user_id: str
    email: EmailStr | str
    name: str
    role: str


class AuthTokens(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: TokenUser


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str
