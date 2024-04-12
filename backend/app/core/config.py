from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    API_V1_STR: str = "/api/v1"

