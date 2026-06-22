from src.core.exceptions import UnauthorizedError
from src.core.security import create_access_token, create_refresh_token, decode_refresh_token
from src.schemas.auth import AuthTokens, TokenUser
from src.utils.enums import RoleEnum


class AuthService:
    def issue_tokens(self, *, user_id: str, email: str, name: str, role: RoleEnum) -> AuthTokens:
        claims = {"email": email, "name": name, "role": role.value}
        access_token = create_access_token(user_id, claims)
        refresh_token = create_refresh_token(user_id, claims)
        return AuthTokens(
            access_token=access_token,
            refresh_token=refresh_token,
            user=TokenUser(user_id=user_id, email=email, name=name, role=role.value),
        )

    def refresh_tokens(self, refresh_token: str) -> AuthTokens:
        try:
            payload = decode_refresh_token(refresh_token)
        except Exception as exc:  # noqa: BLE001
            raise UnauthorizedError("Invalid refresh token") from exc

        if payload.get("type") != "refresh":
            raise UnauthorizedError("Invalid refresh token")

        role = RoleEnum(payload.get("role", RoleEnum.viewer.value))
        return self.issue_tokens(
            user_id=payload["sub"],
            email=payload.get("email", ""),
            name=payload.get("name", ""),
            role=role,
        )
