from fastapi import APIRouter

from src.api.v1 import auth, departures, faqs, inquiries, public_content, testimonials, treks
from src.api.v1.admin import content as admin_content
from src.api.v1.admin import departures as admin_departures, faqs as admin_faqs
from src.api.v1.admin import inquiries as admin_inquiries
from src.api.v1.admin import media as admin_media
from src.api.v1.admin import settings as admin_settings
from src.api.v1.admin import testimonials as admin_testimonials
from src.api.v1.admin import treks as admin_treks

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(public_content.router, tags=["Public Content"])
v1_router.include_router(treks.router, tags=["Treks"])
v1_router.include_router(departures.router, tags=["Departures"])
v1_router.include_router(faqs.router, tags=["FAQs"])
v1_router.include_router(testimonials.router, tags=["Testimonials"])
v1_router.include_router(inquiries.router, tags=["Inquiries"])
v1_router.include_router(auth.router, tags=["Auth"])
v1_router.include_router(admin_treks.router, tags=["Admin Treks"])
v1_router.include_router(admin_departures.router, tags=["Admin Departures"])
v1_router.include_router(admin_faqs.router, tags=["Admin FAQs"])
v1_router.include_router(admin_testimonials.router, tags=["Admin Testimonials"])
v1_router.include_router(admin_content.router, tags=["Admin Content"])
v1_router.include_router(admin_inquiries.router, tags=["Admin Inquiries"])
v1_router.include_router(admin_media.router, tags=["Admin Media"])
v1_router.include_router(admin_settings.router, tags=["Admin Settings"])
