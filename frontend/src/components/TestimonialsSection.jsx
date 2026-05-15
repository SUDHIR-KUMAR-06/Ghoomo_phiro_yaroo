import SectionHeading from "./SectionHeading";

function TestimonialsSection({ testimonials }) {
  return (
    <section className="section">
      <div className="container">
        <SectionHeading
          eyebrow="Testimonials"
          title="Social proof framed like a trusted mountain brand."
          description="The testimonial area keeps the tone reassuring and experience-led, matching the premium trekking trust layer of the source style."
        />

        <div className="testimonials-grid">
          {testimonials.map((testimonial) => (
            <article key={testimonial.name} className="testimonial panel reveal">
              <div className="stars">★★★★★</div>
              <p>{testimonial.quote}</p>
              <div className="person">
                <div className="avatar">{testimonial.initials}</div>
                <div>
                  <strong>{testimonial.name}</strong>
                  <span>{testimonial.route}</span>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default TestimonialsSection;
