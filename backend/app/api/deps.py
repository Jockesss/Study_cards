from app.db.base import Base
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal, async_engine
from loguru import logger


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


async def create_tables():
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("--- THE TABLES ARE SET ---")
    except Exception as e:
        logger.critical(f"Error creating tables: {e}")
