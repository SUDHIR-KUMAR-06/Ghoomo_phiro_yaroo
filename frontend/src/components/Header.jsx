function Header({ isMenuOpen, isScrolled, navLinks, onToggleMenu, onCloseMenu }) {
  return (
    <>
      <header className={`header ${isScrolled ? "scrolled" : ""}`}>
        <div className="container">
          <a href="#top" className="brand">
            <div className="brand-mark">HT</div>
            <div className="brand-text">
              <strong>HIMTREK 2026</strong>
              <span>Adventure Begins Here</span>
            </div>
          </a>

          <nav className="nav" aria-label="Primary navigation">
            {navLinks.map((link) => (
              <a key={link.href} href={link.href}>
                {link.label}
              </a>
            ))}
          </nav>

          <div className="header-actions">
            <a href="#departures" className="btn btn-secondary">
              View Batches
            </a>
            <a href="#cta" className="btn btn-primary">
              Book 2026 Trek
            </a>
            <button
              className={`menu-toggle ${isMenuOpen ? "active" : ""}`}
              type="button"
              aria-label="Toggle mobile menu"
              aria-expanded={isMenuOpen}
              onClick={onToggleMenu}
            >
              <span />
            </button>
          </div>
        </div>
      </header>

      <div className={`mobile-panel ${isMenuOpen ? "open" : ""}`}>
        <div className="mobile-links">
          {navLinks.map((link) => (
            <a key={link.href} href={link.href} onClick={onCloseMenu}>
              {link.label}
            </a>
          ))}
        </div>
        <a href="#cta" className="btn btn-primary mobile-cta" onClick={onCloseMenu}>
          Book 2026 Trek
        </a>
      </div>
    </>
  );
}

export default Header;
