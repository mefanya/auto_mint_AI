import openai
import json
from models.token_model import TokenDetails

openai.api_key = "ТВОЙ_OPENAI_API_КЛЮЧ"

def generate_token_details(prompt: str) -> TokenDetails:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Создай токен по запросу: {prompt}"}]
    )
    data = json.loads(response["choices"][0]["message"]["content"])
    return TokenDetails(name=data["name"], symbol=data["symbol"], supply=data["supply"])
