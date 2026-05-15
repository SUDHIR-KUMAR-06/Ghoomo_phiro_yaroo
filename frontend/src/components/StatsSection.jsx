import SectionHeading from "./SectionHeading";

function StatsSection({ stats }) {
  return (
    <section className="section">
      <div className="container">
        <SectionHeading
          eyebrow="Adventure Statistics"
          title="Built to feel credible, capable, and aspirational."
          description="A stats strip adds the confidence layer typical of modern travel brands while reinforcing social proof and brand maturity."
        />

        <div className="stats-grid">
          {stats.map((stat) => (
            <article key={stat.label} className="stat-card panel reveal" data-stat>
              <strong data-value={stat.value} data-suffix={stat.suffix}>
                0
              </strong>
              <p>{stat.label}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default StatsSection;
