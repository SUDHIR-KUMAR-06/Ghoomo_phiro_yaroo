import logging

from src.repositories.media_repository import MediaRepository
from src.schemas.media import MediaAsset, MediaAssetCreate

logger = logging.getLogger(__name__)


class MediaService:
    def __init__(self, repository: MediaRepository):
        self.repository = repository

    def list_media(self) -> list[MediaAsset]:
        return self.repository.list()

    def create_media(self, payload: MediaAssetCreate) -> MediaAsset:
        logger.info("TODO: replace media metadata stub with real %s upload provider.", payload.provider)
        return self.repository.create_media(payload)

    def delete_media(self, media_id: str) -> bool:
        return self.repository.delete(media_id)
