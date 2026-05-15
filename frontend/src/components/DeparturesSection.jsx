function DeparturesSection({ departures }) {
  return (
    <section className="section" id="departures">
      <div className="container departures-wrap">
        <div className="departures-side panel reveal">
          <div className="eyebrow">Upcoming Departures</div>
          <h3>Bookings open for the 2026 mountain season.</h3>
          <p>
            This section mirrors the practical travel-commerce rhythm of the reference: clear dates,
            route names, quick descriptors, and immediate action.
          </p>
        </div>

        <div className="departures-list">
          {departures.map((departure) => (
            <article key={`${departure.day}-${departure.name}`} className="departure-card panel reveal">
              <div className="departure-date">
                <strong>{departure.day}</strong>
                <span>{departure.month}</span>
              </div>
              <div className="departure-copy">
                <h4>{departure.name}</h4>
                <p>{departure.description}</p>
                <div className="tag-row">
                  {departure.tags.map((tag) => (
                    <span key={tag} className="tag">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
              <a href="#cta" className="btn btn-primary">
                Enroll
              </a>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default DeparturesSection;
