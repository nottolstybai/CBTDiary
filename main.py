from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from starlette.staticfiles import StaticFiles

from db_manager.database import SessionLocal
from routes import routes
# from db_manager.fast_users import fastapi_users

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
app.mount("/scripts", StaticFiles(directory="web/scripts"), name="scripts")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routes)

