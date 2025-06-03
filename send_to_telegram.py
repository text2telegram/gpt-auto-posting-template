
import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TARGET_CHAT_ID")
text = "🚀 Проверка автопубликации через `send_to_telegram.py`"

url = f"https://api.telegram.org/bot{token}/sendMessage"
payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}

response = requests.post(url, json=payload)
print(response.text)

