from cbt_diary import app_routes
from fastapi import APIRouter
import templates
from cbt_diary.export.routes import router as model_router

routes = APIRouter()
routes.include_router(app_routes.router, prefix="/api/diary")
routes.include_router(templates.router, prefix="/app")
routes.include_router(model_router, prefix="/export")
