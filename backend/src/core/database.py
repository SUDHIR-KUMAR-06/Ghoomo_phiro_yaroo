import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.core.config import get_settings

logger = logging.getLogger(__name__)

mongo_client: AsyncIOMotorClient | None = None
mongo_database: AsyncIOMotorDatabase | None = None


async def connect_to_mongo() -> None:
    global mongo_client, mongo_database

    settings = get_settings()
    if settings.use_mock_db:
        logger.info("Running with in-memory repositories because USE_MOCK_DB=true.")
        return

    if not settings.mongodb_uri:
        logger.warning("MongoDB URI is missing. Falling back to mock repositories.")
        return

    mongo_client = AsyncIOMotorClient(settings.mongodb_uri)
    mongo_database = mongo_client[settings.mongodb_database]
    logger.info("MongoDB connection initialized for database '%s'.", settings.mongodb_database)


async def close_mongo_connection() -> None:
    global mongo_client, mongo_database

    if mongo_client is not None:
        mongo_client.close()
        mongo_client = None
        mongo_database = None


def get_database() -> AsyncIOMotorDatabase | None:
    return mongo_database
