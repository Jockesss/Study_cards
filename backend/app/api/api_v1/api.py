from fastapi import APIRouter
from .endpoints import user

# Create an instance of APIRouter
api_router = APIRouter()

api_router.include_router(user.router, prefix='/user', tags=['Auth'])
