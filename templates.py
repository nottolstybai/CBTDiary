from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="web")


@router.get("/diary/{user_id}")
async def get_stocks(request: Request, user_id: str):
    return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id})


@router.get("/diary/record/{record_id}")
async def get_stocks(request: Request, record_id):
    return templates.TemplateResponse("record.html", {"request": request, "record": record_id})


@router.get("/oauth")
async def get_stocks(request: Request):
    return templates.TemplateResponse("oauth.html", {"request": request})


@router.get("/register")
async def get_stocks(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


