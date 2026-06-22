import { useEffect, useMemo, useState } from "react";
import Header from "../components/Header";
import HeroSection from "../components/HeroSection";
import FeaturedTreksSection from "../components/FeaturedTreksSection";
import WhyChooseUsSection from "../components/WhyChooseUsSection";
import DeparturesSection from "../components/DeparturesSection";
import StatsSection from "../components/StatsSection";
import StorytellingSection from "../components/StorytellingSection";
import TestimonialsSection from "../components/TestimonialsSection";
import FAQSection from "../components/FAQSection";
import CtaSection from "../components/CtaSection";
import Footer from "../components/Footer";
import "../styles/landing-page.css";
import "../styles/landing-page-responsive.css";

const trekCards = [
  { badge: "Featured", name: "YulaKanda Trek", duration: "5 Days", altitude: "12,778 ft", difficulty: "Moderate", region: "Kinnaur" },
  { badge: "Popular", name: "Triund Summit Escape", duration: "2 Days", altitude: "9,350 ft", difficulty: "Easy", region: "Dharamshala" },
  { badge: "High Demand", name: "Sar Pass Expedition", duration: "5 Days", altitude: "13,800 ft", difficulty: "Moderate", region: "Kasol" },
  { badge: "Premium", name: "Spiti Valley Traverse", duration: "8 Days", altitude: "15,000 ft", difficulty: "Moderate+", region: "Spiti" },
];

const departures = [
  { day: "01", month: "Jun 2026", name: "YulaKanda Trek", description: "Valley-to-pass crossover with cinematic campsites, alpine transitions, and signature early-season demand.", tags: ["Moderate", "5 Days", "Kinnaur"] },
  { day: "14", month: "Jun 2026", name: "Triund Summit Escape", description: "Beginner-friendly route with high visual reward, ideal for new trekkers wanting a premium first climb.", tags: ["Easy", "2 Days", "Dharamshala"] },
  { day: "28", month: "Jun 2026", name: "Sar Pass Expedition", description: "Forest gradients, snow crossings, and bold group energy for trekkers ready to step beyond the basics.", tags: ["Moderate", "5 Days", "Kasol"] },
  { day: "12", month: "Jul 2026", name: "Spiti Valley Traverse", description: "High-altitude road-and-trail storytelling with monastery landscapes, stark terrain, and premium batch pacing.", tags: ["Moderate+", "8 Days", "Spiti"] },
];

const stats = [
  { value: 4.8, suffix: "/5", label: "Average traveller satisfaction score" },
  { value: 26, suffix: "+", label: "Curated 2026 departures across key regions" },
  { value: 12, suffix: "+", label: "Signature routes from weekend to expedition grade" },
  { value: 100, suffix: "%", label: "Focus on guided, responsive mountain support" },
];

const stories = [
  {
    imageLabel: "image2",
    eyebrow: "Forest Arrival",
    title: "Start where pine air, valley light, and anticipation meet.",
    body: ["The first storytelling block is designed for an atmospheric trail-opening image: something that instantly sells scale, calm, and Himalayan mood."],
    points: [
      "Warm earthy tones with premium editorial spacing",
      "Rounded media framing that softens the rugged subject",
      "High-legibility copy layout for conversion content",
    ],
  },
  {
    imageLabel: "image3",
    eyebrow: "Campfire Evenings",
    title: "Show the human side of the expedition, not just the summit.",
    body: ["This visual slot is ideal for group moments, camps, shelters, or tent clusters: the part of the journey that makes the brand feel trustworthy and lived-in."],
    points: [
      "Balanced text-media rhythm inspired by premium travel landing pages",
      "Soft surfaces and elegant shadow depth for a higher-end feel",
      "Strong responsiveness without losing section drama",
    ],
    reverse: true,
  },
  {
    imageLabel: "image4",
    eyebrow: "Above the Tree Line",
    title: "End on altitude, clarity, and the emotional payoff of the climb.",
    body: ["The final scenic block is set up for your most dramatic frame: summit ridges, high meadows, or wide Himalayan horizons that complete the story arc."],
    points: [
      "Cinematic composition with room for bold messaging",
      "Visual purpose preserved even before real photography is inserted",
      "Designed to carry premium brand emotion into the final CTA",
    ],
  },
];

const testimonials = [
  { initials: "SS", name: "Sankar S.", route: "Triund Departure", quote: "The trip felt smooth, supportive, and beautifully paced. It had the polish of a premium brand without losing the raw mountain spirit." },
  { initials: "AK", name: "Avi K.", route: "Hampta Pass Batch", quote: "Strong guides, clean organisation, and a very memorable route. The overall experience felt confident from booking to summit day." },
  { initials: "JK", name: "Jayaditya K.", route: "Indrahar Route", quote: "The team struck the right balance between safety, encouragement, and atmosphere. It felt thoughtfully designed in every stage." },
];

const whyChooseUs = [
  { number: "01", title: "Experienced trek leadership", text: "Trail guidance, pacing discipline, and route confidence built for first-timers and repeat trekkers alike." },
  { number: "02", title: "Clean itinerary structure", text: "Clear departure planning, altitude framing, and strong visual hierarchy that reduces booking friction." },
  { number: "03", title: "Premium yet grounded stays", text: "Comfort-forward camps, warm hospitality, and an earthy outdoors mood instead of generic luxury styling." },
  { number: "04", title: "Conversion-first experience", text: "Sticky header, direct CTAs, responsive cards, and guided discovery designed for travel enquiries that convert." },
];

const faqs = [
  { question: "Are these treks suitable for beginners?", answer: "Yes. Routes like Triund-style departures work especially well for first-time trekkers looking for a guided, premium-feel introduction." },
  { question: "What is included in a typical 2026 batch?", answer: "Typical inclusions can cover guided support, stay or campsite arrangements, planned meals, route coordination, and batch-level assistance depending on the trek format." },
  { question: "How early should I reserve my spot?", answer: "Popular summer and shoulder-season departures should ideally be reserved early, especially signature routes that combine easy access with strong visual appeal." },
  { question: "Can this design support future real photos easily?", answer: "Yes. Each major image zone is preserved with an exact-sequence placeholder so production photos can be dropped in later without changing layout logic or visual intent." },
];

function LandingPage() {
  const navLinks = useMemo(
    () => [
      { label: "Treks", href: "#featured" },
      { label: "Why Us", href: "#why" },
      { label: "Departures", href: "#departures" },
      { label: "Stories", href: "#stories" },
      { label: "FAQ", href: "#faq" },
      { label: "Contact", href: "#footer" },
    ],
    []
  );
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 24);
    handleScroll();
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    const revealElements = document.querySelectorAll(".reveal");
    const statCards = document.querySelectorAll("[data-stat]");

    const animateNumber = (element) => {
      if (element.dataset.done === "true") return;

      element.dataset.done = "true";
      const target = Number(element.dataset.value);
      const suffix = element.dataset.suffix || "";
      const startTime = performance.now();
      const duration = 1200;

      const updateValue = (now) => {
        const progress = Math.min((now - startTime) / duration, 1);
        const currentValue = target * progress;
        element.textContent = target % 1 === 0 ? `${Math.round(currentValue)}${suffix}` : `${currentValue.toFixed(1)}${suffix}`;
        if (progress < 1) window.requestAnimationFrame(updateValue);
      };

      window.requestAnimationFrame(updateValue);
    };

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("in-view");
          if (entry.target.hasAttribute("data-stat")) {
            const valueElement = entry.target.querySelector("[data-value]");
            if (valueElement) animateNumber(valueElement);
          }
        });
      },
      { threshold: 0.15 }
    );

    revealElements.forEach((element) => observer.observe(element));
    statCards.forEach((element) => observer.observe(element));
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth > 860) setIsMenuOpen(false);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const closeMenu = () => setIsMenuOpen(false);

  return (
    <div className="page-shell">
      <Header
        isMenuOpen={isMenuOpen}
        isScrolled={isScrolled}
        navLinks={navLinks}
        onToggleMenu={() => setIsMenuOpen((current) => !current)}
        onCloseMenu={closeMenu}
      />
      <main id="top">
        <HeroSection />
        <FeaturedTreksSection trekCards={trekCards} />
        <WhyChooseUsSection items={whyChooseUs} />
        <DeparturesSection departures={departures} />
        <StatsSection stats={stats} />
        <StorytellingSection stories={stories} />
        <TestimonialsSection testimonials={testimonials} />
        <FAQSection faqs={faqs} />
        <CtaSection />
      </main>
      <Footer navLinks={navLinks} />
    </div>
  );
}

export default LandingPage;
