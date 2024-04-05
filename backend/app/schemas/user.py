from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str
    password: str
    email: str
    is_superuser: bool | None = Field()


class UserCreate(UserBase):
    username: str
    password: str
    email: str
