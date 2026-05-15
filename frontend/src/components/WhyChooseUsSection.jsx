import SectionHeading from "./SectionHeading";

function WhyChooseUsSection({ items }) {
  return (
    <section className="section" id="why">
      <div className="container">
        <SectionHeading
          eyebrow="Why Choose Us"
          title="Grounded mountain operations with a polished premium feel."
          description="The design language leans on forest tones, soft glass surfaces, rounded cards, and elegant shadows to echo a modern Himalayan brand."
        />

        <div className="why-grid">
          {items.map((item) => (
            <article key={item.number} className="why-card panel reveal">
              <div className="icon">{item.number}</div>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default WhyChooseUsSection;
