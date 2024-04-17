from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    API_V1_STR: str = "/v1"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:qwe123@localhost:5432/cards"
    LOGGER: str = "local"


settings = Setting()
