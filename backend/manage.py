from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.api.deps import create_tables
from loguru import logger

from app.core.config import Setting
from app.core.logs import LoggerConfigurator

# List of origins that are allowed to make cross-origin requests
origins: list[str] = [
    "http://localhost:3000",
]

_settings: Setting = Setting()


async def lifespan(app: FastAPI):
    LoggerConfigurator.setup_logging()
    await create_tables()
    logger.info(f"FILE ENV USING -----> .env == {_settings.LOGGER} ")
    yield
    logger.info("--- Stop application ---")


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    app.include_router(api_router, prefix='/v1')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


logger.info("--- Starting application ---")
