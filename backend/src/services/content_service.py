from src.core.exceptions import NotFoundError
from src.repositories.content_repository import ContentRepository
from src.repositories.departure_repository import DepartureRepository
from src.repositories.faq_repository import FAQRepository
from src.repositories.testimonial_repository import TestimonialRepository
from src.repositories.trek_repository import TrekRepository
from src.schemas.departure import Departure
from src.schemas.faq import FAQItem
from src.schemas.landing_page import LandingPageContentUpdate, LandingPageResponse
from src.schemas.testimonial import TestimonialItem
from src.schemas.trek import TrekListItem


class ContentService:
    def __init__(
        self,
        content_repository: ContentRepository,
        trek_repository: TrekRepository,
        departure_repository: DepartureRepository,
        faq_repository: FAQRepository,
        testimonial_repository: TestimonialRepository,
    ):
        self.content_repository = content_repository
        self.trek_repository = trek_repository
        self.departure_repository = departure_repository
        self.faq_repository = faq_repository
        self.testimonial_repository = testimonial_repository

    def get_landing_page(self) -> LandingPageResponse:
        return self.content_repository.get_landing_page()

    def update_landing_page(self, payload: LandingPageContentUpdate) -> LandingPageResponse:
        return self.content_repository.update_landing_page(payload.model_dump(exclude_none=True))

    def get_treks(self, **filters) -> list[TrekListItem]:
        return self.trek_repository.list_filtered(**filters)

    def get_trek_by_slug(self, slug: str) -> TrekListItem:
        trek = self.trek_repository.get_by_slug(slug)
        if trek is None:
            raise NotFoundError("Trek not found")
        return trek

    def get_departures(self, **filters) -> list[Departure]:
        return self.departure_repository.list_filtered(**filters)

    def get_faqs(self) -> list[FAQItem]:
        return sorted(self.faq_repository.list(), key=lambda item: item.sort_order)

    def get_testimonials(self) -> list[TestimonialItem]:
        return self.testimonial_repository.list()
