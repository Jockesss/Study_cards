from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]
    is_superuser: bool | None = Field(False, alias='is_superuser')


class UserCreate(UserBase):
    username: str
    password: str
    email: str
