from pydantic import BaseModel
from typing import List

class TokenRequest(BaseModel):
    prompt: str
    wallets: List[str]  # Список кошельков

class TokenDetails(BaseModel):
    name: str
    symbol: str
    supply: int
