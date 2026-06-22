from datetime import date, datetime, timezone

from src.schemas.departure import Departure
from src.schemas.faq import FAQItem
from src.schemas.landing_page import (
    CTAAction,
    CTAContent,
    FooterContent,
    HeroMetric,
    HeroSection,
    LandingPageResponse,
    SearchHighlight,
    StatItem,
    StoryBlock,
    WhyChooseUsItem,
)
from src.schemas.media import MediaAsset
from src.schemas.testimonial import TestimonialItem
from src.schemas.trek import TrekListItem
from src.utils.enums import DifficultyEnum


def build_seed_data() -> dict[str, object]:
    now = datetime.now(timezone.utc)

    hero_image = MediaAsset(
        id="media-image1",
        label="image1",
        url=None,
        alt="Hero trek visual",
        created_at=now,
        updated_at=now,
    )
    story_images = [
        MediaAsset(id="media-image2", label="image2", alt="Story block one", created_at=now, updated_at=now),
        MediaAsset(id="media-image3", label="image3", alt="Story block two", created_at=now, updated_at=now),
        MediaAsset(id="media-image4", label="image4", alt="Story block three", created_at=now, updated_at=now),
    ]

    treks = [
        TrekListItem(id="trek-1", name="YulaKanda Trek", slug="yulakanda-trek", badge="Featured", duration_days=5, altitude_ft=12778, difficulty=DifficultyEnum.moderate, region="Kinnaur", batch_year=2026, summary="Valley-to-pass crossover with cinematic campsites, alpine transitions, and signature early-season demand.", hero_image=None, is_featured=True, created_at=now, updated_at=now),
        TrekListItem(id="trek-2", name="Triund Summit Escape", slug="triund-summit-escape", badge="Popular", duration_days=2, altitude_ft=9350, difficulty=DifficultyEnum.easy, region="Dharamshala", batch_year=2026, summary="Beginner-friendly route with high visual reward, ideal for new trekkers wanting a premium first climb.", hero_image=None, is_featured=True, created_at=now, updated_at=now),
        TrekListItem(id="trek-3", name="Sar Pass Expedition", slug="sar-pass-expedition", badge="High Demand", duration_days=5, altitude_ft=13800, difficulty=DifficultyEnum.moderate, region="Kasol", batch_year=2026, summary="Forest gradients, snow crossings, and bold group energy for trekkers ready to step beyond the basics.", hero_image=None, is_featured=True, created_at=now, updated_at=now),
        TrekListItem(id="trek-4", name="Spiti Valley Traverse", slug="spiti-valley-traverse", badge="Premium", duration_days=8, altitude_ft=15000, difficulty=DifficultyEnum.moderate_plus, region="Spiti", batch_year=2026, summary="High-altitude road-and-trail storytelling with monastery landscapes, stark terrain, and premium batch pacing.", hero_image=None, is_featured=True, created_at=now, updated_at=now),
    ]

    departures = [
        Departure(id="dep-1", trek_id="trek-1", trek_name="YulaKanda Trek", departure_date=date(2026, 6, 1), month_label="Jun 2026", summary=treks[0].summary, tags=["Moderate", "5 Days", "Kinnaur"], seats_total=None, seats_available=None, created_at=now, updated_at=now),
        Departure(id="dep-2", trek_id="trek-2", trek_name="Triund Summit Escape", departure_date=date(2026, 6, 14), month_label="Jun 2026", summary=treks[1].summary, tags=["Easy", "2 Days", "Dharamshala"], seats_total=None, seats_available=None, created_at=now, updated_at=now),
        Departure(id="dep-3", trek_id="trek-3", trek_name="Sar Pass Expedition", departure_date=date(2026, 6, 28), month_label="Jun 2026", summary=treks[2].summary, tags=["Moderate", "5 Days", "Kasol"], seats_total=None, seats_available=None, created_at=now, updated_at=now),
        Departure(id="dep-4", trek_id="trek-4", trek_name="Spiti Valley Traverse", departure_date=date(2026, 7, 12), month_label="Jul 2026", summary=treks[3].summary, tags=["Moderate+", "8 Days", "Spiti"], seats_total=None, seats_available=None, created_at=now, updated_at=now),
    ]

    faqs = [
        FAQItem(id="faq-1", question="Are these treks suitable for beginners?", answer="Yes. Routes like Triund-style departures work especially well for first-time trekkers looking for a guided, premium-feel introduction.", sort_order=1, is_active=True, created_at=now, updated_at=now),
        FAQItem(id="faq-2", question="What is included in a typical 2026 batch?", answer="Typical inclusions can cover guided support, stay or campsite arrangements, planned meals, route coordination, and batch-level assistance depending on the trek format.", sort_order=2, is_active=True, created_at=now, updated_at=now),
        FAQItem(id="faq-3", question="How early should I reserve my spot?", answer="Popular summer and shoulder-season departures should ideally be reserved early, especially signature routes that combine easy access with strong visual appeal.", sort_order=3, is_active=True, created_at=now, updated_at=now),
        FAQItem(id="faq-4", question="Can this design support future real photos easily?", answer="Yes. Each major image zone is preserved with an exact-sequence placeholder so production photos can be dropped in later without changing layout logic or visual intent.", sort_order=4, is_active=True, created_at=now, updated_at=now),
    ]

    testimonials = [
        TestimonialItem(id="test-1", name="Sankar S.", initials="SS", route_label="Triund Departure", rating=5, quote="The trip felt smooth, supportive, and beautifully paced. It had the polish of a premium brand without losing the raw mountain spirit.", is_featured=True, created_at=now, updated_at=now),
        TestimonialItem(id="test-2", name="Avi K.", initials="AK", route_label="Hampta Pass Batch", rating=5, quote="Strong guides, clean organisation, and a very memorable route. The overall experience felt confident from booking to summit day.", is_featured=True, created_at=now, updated_at=now),
        TestimonialItem(id="test-3", name="Jayaditya K.", initials="JK", route_label="Indrahar Route", rating=5, quote="The team struck the right balance between safety, encouragement, and atmosphere. It felt thoughtfully designed in every stage.", is_featured=True, created_at=now, updated_at=now),
    ]

    landing_page = LandingPageResponse(
        hero=HeroSection(
            eyebrow="Himalayan Treks • Road Trips • Premium Departures",
            title="Adventure Begins Here.",
            description="A cinematic Himalayan travel landing page inspired by premium trekking brands: bold typography, earthy depth, layered sections, and conversion-first journey design.",
            primary_cta=CTAAction(label="Explore Treks", action="scroll", target="#featured"),
            secondary_cta=CTAAction(label="See the Journey", action="scroll", target="#stories"),
            metrics=[
                HeroMetric(label="Traveller Rating", value="4.8/5"),
                HeroMetric(label="Open Batches", value="2026"),
                HeroMetric(label="Premium Guidance", value="Small Groups"),
            ],
            image=hero_image,
        ),
        search_highlights=[
            SearchHighlight(label="Destination", value="Himachal & Uttarakhand", description="Curated premium trekking regions"),
            SearchHighlight(label="Travel Window", value="June to October", description="Best departures for 2026"),
            SearchHighlight(label="Difficulty", value="Easy to Challenging", description="Choose your perfect climb"),
            SearchHighlight(label="Style", value="Guided Small Groups", description="Safety-first mountain operations"),
        ],
        featured_treks=treks,
        why_choose_us=[
            WhyChooseUsItem(number="01", title="Experienced trek leadership", text="Trail guidance, pacing discipline, and route confidence built for first-timers and repeat trekkers alike."),
            WhyChooseUsItem(number="02", title="Clean itinerary structure", text="Clear departure planning, altitude framing, and strong visual hierarchy that reduces booking friction."),
            WhyChooseUsItem(number="03", title="Premium yet grounded stays", text="Comfort-forward camps, warm hospitality, and an earthy outdoors mood instead of generic luxury styling."),
            WhyChooseUsItem(number="04", title="Conversion-first experience", text="Sticky header, direct CTAs, responsive cards, and guided discovery designed for travel enquiries that convert."),
        ],
        departures=departures,
        stats=[
            StatItem(value=4.8, suffix="/5", label="Average traveller satisfaction score"),
            StatItem(value=26, suffix="+", label="Curated 2026 departures across key regions"),
            StatItem(value=12, suffix="+", label="Signature routes from weekend to expedition grade"),
            StatItem(value=100, suffix="%", label="Focus on guided, responsive mountain support"),
        ],
        stories=[
            StoryBlock(image_label="image2", eyebrow="Forest Arrival", title="Start where pine air, valley light, and anticipation meet.", body=["The first storytelling block is designed for an atmospheric trail-opening image: something that instantly sells scale, calm, and Himalayan mood."], points=["Warm earthy tones with premium editorial spacing", "Rounded media framing that softens the rugged subject", "High-legibility copy layout for conversion content"], reverse=False, image=story_images[0]),
            StoryBlock(image_label="image3", eyebrow="Campfire Evenings", title="Show the human side of the expedition, not just the summit.", body=["This visual slot is ideal for group moments, camps, shelters, or tent clusters: the part of the journey that makes the brand feel trustworthy and lived-in."], points=["Balanced text-media rhythm inspired by premium travel landing pages", "Soft surfaces and elegant shadow depth for a higher-end feel", "Strong responsiveness without losing section drama"], reverse=True, image=story_images[1]),
            StoryBlock(image_label="image4", eyebrow="Above the Tree Line", title="End on altitude, clarity, and the emotional payoff of the climb.", body=["The final scenic block is set up for your most dramatic frame: summit ridges, high meadows, or wide Himalayan horizons that complete the story arc."], points=["Cinematic composition with room for bold messaging", "Visual purpose preserved even before real photography is inserted", "Designed to carry premium brand emotion into the final CTA"], reverse=False, image=story_images[2]),
        ],
        testimonials=testimonials,
        faqs=faqs,
        cta_strip=CTAContent(eyebrow="Final CTA", title="Your 2026 Himalayan story starts with one departure.", description="Keep the momentum high with a premium CTA strip that feels editorial, cinematic, and decisively travel-focused."),
        footer=FooterContent(contact_email="info@himtrek.co.in", contact_phone="+91 85809 04609", locations=["Delhi", "Himachal", "Uttarakhand"]),
    )

    return {
        "landing_page": landing_page,
        "treks": treks,
        "departures": departures,
        "faqs": faqs,
        "testimonials": testimonials,
        "inquiries": [],
        "media": [hero_image, *story_images],
    }
