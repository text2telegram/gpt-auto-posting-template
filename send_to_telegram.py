
import requests
import os

def send_post(hook, lesson, audio_path):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TARGET_CHAT_ID")

    # Отправляем текст
    text = f"{hook}\n\n{lesson}\n\n👉 Подпишись!"
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
        "chat_id": chat_id,
        "text": text
    })

    # Отправляем аудио
    with open(audio_path, "rb") as audio_file:
        requests.post(f"https://api.telegram.org/bot{token}/sendAudio", data={
            "chat_id": chat_id
        }, files={"audio": audio_file})
