from src.repositories.base import InMemoryRepository
from src.schemas.landing_page import LandingPageResponse


class ContentRepository:
    def __init__(self, content: LandingPageResponse):
        self._content = content

    def get_landing_page(self) -> LandingPageResponse:
        return self._content.model_copy(deep=True)

    def update_landing_page(self, updates: dict) -> LandingPageResponse:
        content = self._content.model_copy(deep=True)

        if updates.get("hero_title"):
            content.hero.title = updates["hero_title"]
        if updates.get("hero_description"):
            content.hero.description = updates["hero_description"]
        if updates.get("cta_title"):
            content.cta_strip.title = updates["cta_title"]
        if updates.get("cta_description"):
            content.cta_strip.description = updates["cta_description"]

        self._content = content
        return self._content.model_copy(deep=True)
