
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_hook():
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": "Создай цепляющий AI-хук для Telegram (до 20 слов)"}]
    )
    return response.choices[0].message["content"].strip()

def generate_lesson():
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": "Напиши полезный пост в Telegram стиле (AI, крипта, хак, до 600 зн)"}]
    )
    return response.choices[0].message["content"].strip()
