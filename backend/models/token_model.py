from pydantic import BaseModel
from typing import List

class TokenRequest(BaseModel):
    prompt: str

class TokenDetails(BaseModel):
    name: str
    symbol: str
    supply: int
