from pydantic import BaseModel

from src.schemas.departure import Departure
from src.schemas.faq import FAQItem
from src.schemas.media import MediaAsset
from src.schemas.testimonial import TestimonialItem
from src.schemas.trek import TrekListItem


class CTAAction(BaseModel):
    label: str
    action: str
    target: str


class HeroMetric(BaseModel):
    label: str
    value: str


class SearchHighlight(BaseModel):
    label: str
    value: str
    description: str


class WhyChooseUsItem(BaseModel):
    number: str
    title: str
    text: str


class StatItem(BaseModel):
    value: float
    suffix: str
    label: str


class StoryBlock(BaseModel):
    image_label: str
    eyebrow: str
    title: str
    body: list[str]
    points: list[str]
    reverse: bool = False
    image: MediaAsset | None = None


class CTAContent(BaseModel):
    eyebrow: str
    title: str
    description: str


class FooterContent(BaseModel):
    contact_email: str
    contact_phone: str
    locations: list[str]


class HeroSection(BaseModel):
    eyebrow: str
    title: str
    description: str
    primary_cta: CTAAction
    secondary_cta: CTAAction
    metrics: list[HeroMetric]
    image: MediaAsset


class LandingPageResponse(BaseModel):
    hero: HeroSection
    search_highlights: list[SearchHighlight]
    featured_treks: list[TrekListItem]
    why_choose_us: list[WhyChooseUsItem]
    departures: list[Departure]
    stats: list[StatItem]
    stories: list[StoryBlock]
    testimonials: list[TestimonialItem]
    faqs: list[FAQItem]
    cta_strip: CTAContent
    footer: FooterContent


class LandingPageContentUpdate(BaseModel):
    hero_title: str | None = None
    hero_description: str | None = None
    cta_title: str | None = None
    cta_description: str | None = None
