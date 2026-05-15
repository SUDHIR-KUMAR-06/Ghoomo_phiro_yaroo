function Footer({ navLinks }) {
  return (
    <footer className="footer" id="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand reveal">
            <strong>HIMTREK 2026</strong>
            <p>
              A premium Himalayan adventure landing page with responsive structure, sticky transparent
              navigation, elegant section layering, and image-ready placeholders prepared for future
              photography.
            </p>
          </div>

          <div className="reveal">
            <h4>Explore</h4>
            <ul>
              {navLinks.slice(0, 4).map((link) => (
                <li key={link.href}>
                  <a href={link.href}>{link.label}</a>
                </li>
              ))}
            </ul>
          </div>

          <div className="reveal">
            <h4>Categories</h4>
            <ul>
              <li><a href="#featured">Easy Treks</a></li>
              <li><a href="#featured">Moderate Routes</a></li>
              <li><a href="#featured">Premium Batches</a></li>
              <li><a href="#featured">Road Journeys</a></li>
            </ul>
          </div>

          <div className="reveal">
            <h4>Contact</h4>
            <ul>
              <li>info@himtrek.co.in</li>
              <li>+91 85809 04609</li>
              <li>Delhi • Himachal • Uttarakhand</li>
              <li>Instagram • Facebook • YouTube</li>
            </ul>
          </div>
        </div>

        <div className="footer-bottom">
          <span>© Copyright HIMTREK 2026</span>
          <span>Adventure Begins Here</span>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
