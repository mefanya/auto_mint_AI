from openai import OpenAI
from ..models.token_model import TokenDetails
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPEN_AI_API_KEY"),
)


def generate_token_details(prompt: str) -> TokenDetails:
    time.sleep(10)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Создайте токен по запросу: {prompt}"}],
    )
    data = json.loads(response["choices"][0]["message"]["content"])
    return TokenDetails(name=data["name"], symbol=data["symbol"], supply=data["supply"])
