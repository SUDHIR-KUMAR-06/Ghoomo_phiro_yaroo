import { useState } from "react";

function FAQSection({ faqs }) {
  const [openIndex, setOpenIndex] = useState(0);

  return (
    <section className="section" id="faq">
      <div className="container faq-wrap">
        <div className="faq-side panel reveal">
          <div className="eyebrow">FAQ</div>
          <h2>Everything a first-time or returning trekker wants to know.</h2>
          <p>
            A responsive accordion keeps the page interactive and polished while reducing uncertainty
            before booking.
          </p>
        </div>

        <div className="faq-list">
          {faqs.map((faq, index) => {
            const isOpen = openIndex === index;

            return (
              <article key={faq.question} className={`faq-item panel reveal ${isOpen ? "open" : ""}`.trim()}>
                <button
                  className="faq-question"
                  type="button"
                  aria-expanded={isOpen}
                  onClick={() => setOpenIndex(isOpen ? -1 : index)}
                >
                  <span>{faq.question}</span>
                  <span>+</span>
                </button>
                <div className="faq-answer" style={{ maxHeight: isOpen ? "180px" : "0px" }}>
                  <p>{faq.answer}</p>
                </div>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default FAQSection;
