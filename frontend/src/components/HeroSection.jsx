import ImagePlaceholder from "./ImagePlaceholder";
import image1 from "../assets/images/image1.jpeg";

function HeroSection() {
  return (
    <>
      <section className="hero">
        <div className="hero-mountains" />
        <div className="container hero-grid">
          <div className="hero-copy reveal">
            <div className="eyebrow">Himalayan Treks • Road Trips • Premium Departures</div>
            <h1>Adventure Begins Here.</h1>
            <p>
              A cinematic Himalayan travel landing page inspired by premium trekking brands:
              bold typography, earthy depth, layered sections, and conversion-first journey design.
            </p>

            <div className="hero-actions-row">
              <a href="#featured" className="btn btn-primary">
                Explore Treks
              </a>
              <a href="#stories" className="btn btn-secondary">
                See the Journey
              </a>
            </div>

            <div className="hero-meta">
              <div className="hero-meta-item">
                <strong>4.8/5</strong>
                <span>Traveller Rating</span>
              </div>
              <div className="hero-meta-item">
                <strong>2026</strong>
                <span>Open Batches</span>
              </div>
              <div className="hero-meta-item">
                <strong>Small Groups</strong>
                <span>Premium Guidance</span>
              </div>
            </div>
          </div>

          <div className="hero-visual reveal">
            <ImagePlaceholder  src={image1} label="image1" className="hero-image" />
            <div className="floating-card float-a">
              <strong>12+ Curated Routes</strong>
              <span>From weekend escapes to high-altitude classics</span>
            </div>
            <div className="floating-card float-b">
              <strong>Forest to Snowline</strong>
              <span>Grounded, cinematic, Himalayan storytelling</span>
            </div>
          </div>
        </div>
      </section>

      <section className="search-card">
        <div className="container">
          <div className="search-shell reveal">
            <div className="search-field">
              <label>Destination</label>
              <strong>Himachal & Uttarakhand</strong>
              <span>Curated premium trekking regions</span>
            </div>
            <div className="search-field">
              <label>Travel Window</label>
              <strong>June to October</strong>
              <span>Best departures for 2026</span>
            </div>
            <div className="search-field">
              <label>Difficulty</label>
              <strong>Easy to Challenging</strong>
              <span>Choose your perfect climb</span>
            </div>
            <div className="search-field">
              <label>Style</label>
              <strong>Guided Small Groups</strong>
              <span>Safety-first mountain operations</span>
            </div>
            <a href="#departures" className="btn btn-primary">
              Search Treks
            </a>
          </div>
        </div>
      </section>
    </>
  );
}

export default HeroSection;
