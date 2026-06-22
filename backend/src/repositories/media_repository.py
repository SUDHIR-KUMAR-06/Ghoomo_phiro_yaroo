from src.repositories.base import InMemoryRepository
from src.schemas.media import MediaAsset, MediaAssetCreate


class MediaRepository(InMemoryRepository[MediaAsset]):
    def create_media(self, payload: MediaAssetCreate) -> MediaAsset:
        return self.create(MediaAsset, payload.model_dump())
