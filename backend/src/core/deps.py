from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.core.exceptions import ForbiddenError, UnauthorizedError
from src.core.security import decode_access_token
from src.schemas.auth import TokenUser
from src.utils.enums import RoleEnum

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> TokenUser:
    if credentials is None:
        raise UnauthorizedError("Missing bearer token")

    try:
        payload = decode_access_token(credentials.credentials)
    except Exception as exc:  # noqa: BLE001
        raise UnauthorizedError("Invalid access token") from exc

    role = payload.get("role", RoleEnum.viewer.value)
    return TokenUser(
        user_id=payload["sub"],
        email=payload.get("email", ""),
        name=payload.get("name", ""),
        role=role,
    )


def require_roles(*allowed_roles: RoleEnum):
    def dependency(current_user: TokenUser = Depends(get_current_user)) -> TokenUser:
        allowed = {role.value for role in allowed_roles}
        if current_user.role not in allowed:
            raise ForbiddenError("You do not have permission to perform this action")
        return current_user

    return dependency
