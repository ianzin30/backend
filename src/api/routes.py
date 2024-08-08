from fastapi import APIRouter
from src.api import activity

api_router = APIRouter()

api_router.include_router(activity.router, prefix='/activity', tags=['activity'])