from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import api_router
from src.core.config import get_settings
from src.core.database import close_mongo_connection, connect_to_mongo
from src.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_logging()
    await connect_to_mongo()
    yield
    await close_mongo_connection()


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
      title=settings.app_name,
      version=settings.app_version,
      description="Modular FastAPI backend for the HIMTREK 2026 landing page.",
      lifespan=lifespan,
    )

    app.add_middleware(
      CORSMiddleware,
      allow_origins=settings.allowed_origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
    )

    app.include_router(api_router)
    return app


app = create_app()
