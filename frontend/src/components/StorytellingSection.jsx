import ImagePlaceholder from "./ImagePlaceholder";
import SectionHeading from "./SectionHeading";

function StorytellingSection({ stories }) {
  return (
    <section className="section" id="stories">
      <div className="container">
        <SectionHeading
          eyebrow="Scenic Storytelling"
          title="Layered visual blocks for the premium trekking narrative."
          description="These image zones stay intact as styled placeholders so your future photography can drop into the exact intended roles."
        />

        <div className="story-stack">
          {stories.map((story) => (
            <article
              key={story.imageLabel}
              className={`story-block panel reveal ${story.reverse ? "reverse" : ""}`.trim()}
            >
              <div className="story-media">
                <ImagePlaceholder label={story.imageLabel} />
              </div>
              <div className="story-copy">
                <div className="eyebrow">{story.eyebrow}</div>
                <h3>{story.title}</h3>
                {story.body.map((paragraph) => (
                  <p key={paragraph}>{paragraph}</p>
                ))}
                <div className="story-points">
                  {story.points.map((point) => (
                    <div key={point}>{point}</div>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default StorytellingSection;
