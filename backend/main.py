from fastapi import FastAPI
from models.token_model import TokenRequest
from services.ai_service import generate_token_details
from services.blockchain import deploy_token

app = FastAPI()

@app.post("/create_token")
async def create_token(request: TokenRequest):
    token_details = generate_token_details(request.prompt)
    tx_hash = deploy_token(token_details)
    return {"tx_hash": tx_hash, "token_details": token_details}
