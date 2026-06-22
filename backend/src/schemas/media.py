from pydantic import BaseModel

from src.schemas.common import BaseDocument


class MediaAsset(BaseDocument):
    label: str
    url: str | None = None
    alt: str | None = None
    provider: str = "local"


class MediaAssetCreate(BaseModel):
    label: str
    url: str | None = None
    alt: str | None = None
    provider: str = "local"
