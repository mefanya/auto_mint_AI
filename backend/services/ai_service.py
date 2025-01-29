import openai
import json
from ..models.token_model import TokenDetails
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

def generate_token_details(prompt: str) -> TokenDetails:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Создай токен по запросу: {prompt}"}]
    )
    data = json.loads(response["choices"][0]["message"]["content"])
    return TokenDetails(name=data["name"], symbol=data["symbol"], supply=data["supply"])
