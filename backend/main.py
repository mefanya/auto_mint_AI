from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .models.token_model import TokenRequest, TokenDetails
from .services.ai_service import generate_token_details
from .services.blockchain import deploy_token

app = FastAPI()
templates = Jinja2Templates(directory="backend/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_token", response_model=TokenDetails)
async def generate_token(data: TokenRequest):
    """Обрабатывает промт и кошельки, генерирует токен с помощью AI"""
    token_details = generate_token_details(data.prompt)
    return token_details


@app.post("/deploy_token")
async def deploy_token_endpoint(data: TokenRequest):
    """Деплоит токен на блокчейн"""
    token_details = generate_token_details(data.prompt)
    tx_hash = deploy_token(token_details)
    return {"tx_hash": tx_hash, "token_details": token_details}
