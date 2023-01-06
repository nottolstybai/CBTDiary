from cbt_diary import app_routes
from fastapi import APIRouter
import templates

routes = APIRouter()
routes.include_router(app_routes.router, prefix="/api/diary")
routes.include_router(templates.router, prefix="/app")
