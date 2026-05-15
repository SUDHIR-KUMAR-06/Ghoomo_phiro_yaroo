import SectionHeading from "./SectionHeading";

function FeaturedTreksSection({ trekCards }) {
  return (
    <section className="section" id="featured">
      <div className="container">
        <SectionHeading
          eyebrow="Featured Treks"
          title="Signature Himalayan departures for 2026."
          description="Trek cards are kept clean and data-rich to mirror a conversion-focused travel UI: strong hierarchy, crisp specs, and clear booking intent."
        />

        <div className="featured-grid">
          {trekCards.map((trek) => (
            <article key={trek.name} className="trek-card panel reveal">
              <div className="card-top">
                <span className="pill soft">{trek.badge}</span>
                <span className="pill year">Batch 2026</span>
              </div>
              <h3>{trek.name}</h3>
              <div className="trek-meta">
                <div>
                  <span>Duration</span>
                  <strong>{trek.duration}</strong>
                </div>
                <div>
                  <span>Altitude</span>
                  <strong>{trek.altitude}</strong>
                </div>
                <div>
                  <span>Difficulty</span>
                  <strong>{trek.difficulty}</strong>
                </div>
                <div>
                  <span>Region</span>
                  <strong>{trek.region}</strong>
                </div>
              </div>
              <a href="#cta" className="btn btn-primary">
                Reserve Spot
              </a>
            </article>
          ))}
        </div>

        <div className="cta-banner panel reveal">
          <div>
            <h3>Beyond work, beyond limits.</h3>
            <p>
              A branded CTA banner inspired by premium travel homepages: ideal for corporate offsites,
              curated team departures, and high-trust enquiry conversion.
            </p>
          </div>
          <a href="#cta" className="btn btn-primary">
            Plan Corporate Trek
          </a>
        </div>
      </div>
    </section>
  );
}

export default FeaturedTreksSection;
