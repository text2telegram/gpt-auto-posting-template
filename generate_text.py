
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_hook():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Создай цепляющий АИ-хук для Telegram (до 20 слов)"}]
    )
    return response.choices[0].message.content.strip()

def generate_lesson():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Напиши полезный пост в Telegram стиле (АИ, крипта, хак, до 600 зн)"}]
    )
    return response.choices[0].message.content.strip()
