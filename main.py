
import os
import time
from generate_text import generate_text
from generate_voice import generate_voice
from send_to_telegram import send_post

# Проверка ключа OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY не найден! Завершаем...")
    exit(1)
print("✅ OPENAI_API_KEY загружен успешно.")

# Старт цикла
print("🚀 Main.py started: begin posting cycle...")

while True:
    try:
        print("✍️ Generating text...")
        generate_text()

        print("🎤 Generating voice...")
        generate_voice()

        print("📬 Sending to Telegram...")
        send_post()

    except Exception as e:
        print(f"❌ Ошибка в процессе публикации: {e}")

    print("⏳ Жду 24 часа до следующей публикации...")
    time.sleep(86400)  # 24 часа







