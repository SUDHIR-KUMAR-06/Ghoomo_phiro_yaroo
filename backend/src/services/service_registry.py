from functools import lru_cache

from src.repositories.content_repository import ContentRepository
from src.repositories.departure_repository import DepartureRepository
from src.repositories.faq_repository import FAQRepository
from src.repositories.inquiry_repository import InquiryRepository
from src.repositories.media_repository import MediaRepository
from src.repositories.testimonial_repository import TestimonialRepository
from src.repositories.trek_repository import TrekRepository
from src.seed.seed_demo_content import build_seed_data
from src.services.auth_service import AuthService
from src.services.content_service import ContentService
from src.services.google_oauth_service import GoogleOAuthService
from src.services.inquiry_service import InquiryService
from src.services.media_service import MediaService


class ServiceRegistry:
    def __init__(self):
        seed = build_seed_data()
        self.trek_repository = TrekRepository(seed["treks"])
        self.departure_repository = DepartureRepository(seed["departures"])
        self.faq_repository = FAQRepository(seed["faqs"])
        self.testimonial_repository = TestimonialRepository(seed["testimonials"])
        self.inquiry_repository = InquiryRepository(seed["inquiries"])
        self.media_repository = MediaRepository(seed["media"])
        self.content_repository = ContentRepository(seed["landing_page"])

        self.content_service = ContentService(
            self.content_repository,
            self.trek_repository,
            self.departure_repository,
            self.faq_repository,
            self.testimonial_repository,
        )
        self.inquiry_service = InquiryService(self.inquiry_repository)
        self.media_service = MediaService(self.media_repository)
        self.auth_service = AuthService()
        self.google_oauth_service = GoogleOAuthService(self.auth_service)


@lru_cache
def get_registry() -> ServiceRegistry:
    return ServiceRegistry()
