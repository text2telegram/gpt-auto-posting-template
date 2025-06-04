
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TARGET_CHAT_ID")
TEXT = os.getenv("POST_TEXT", "🧠 SmartTestBot готов!")

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": TEXT, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    print(response.text)

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(86400)  # каждые 24 часа


