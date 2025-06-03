
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_post(hook, lesson, audio_path):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TARGET_CHAT_ID")

    text = f"📌 {hook}\n\n{lesson}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)
