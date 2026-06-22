# Backend

FastAPI backend scaffold for the HIMTREK 2026 frontend.

## What Is Fully Implemented
- App bootstrap with versioned API routing
- Public landing page, trek, departure, FAQ, testimonial, and inquiry endpoints
- Modular in-memory repositories seeded from frontend-equivalent content
- JWT helpers and Google OAuth-ready auth scaffolding
- Admin-protected CRUD routes for content, treks, departures, testimonials, FAQs, inquiries, and media metadata
- `.env.example` and basic tests

## What Is Partially Implemented With Placeholders
- MongoDB connection bootstrap exists, but the app currently runs against in-memory repositories by default
- Google OAuth callback supports mock mode for local development
- Media upload is metadata-only until a real provider is chosen
- Notification handling is a TODO stub
- User persistence and audit logging are placeholders for the next phase

## Blocked Items Requiring Your Input
- Final Google OAuth client credentials and redirect URI
- Whether customer auth is needed or admin-only auth is enough
- Media storage provider choice: local, S3, or Cloudinary
- Notification provider choice: email, WhatsApp, CRM, or none
- Whether booking CTAs should remain inquiries or become reservation/payment flows

## Run
1. Create a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`.
4. Start the API:
   `uvicorn src.main:app --reload`
5. Run tests:
   `pytest`

## Placeholder Notes
- `USE_MOCK_DB=true` keeps the backend runnable without MongoDB.
- TODO: set `USE_MOCK_DB=false` and wire real Mongo repositories when ready.
- TODO: add Google OAuth credentials in `.env` before enabling real OAuth.
- TODO: replace media and notification stubs with real providers.
