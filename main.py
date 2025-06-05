
import os
import time
from dotenv import load_dotenv
from generate_text import generate_text
from generate_voice import generate_voice
from send_to_telegram import send_post

# Загружаем .env-файл
env_file = os.getenv("ENV_FILE", ".env.smarttest")
load_dotenv(env_file)
print(f"✅ Loaded env file: {env_file}")

# Бесконечный цикл публикаций
while True:
    print("🚀 Main.py started: begin posting cycle...")

    try:
        print("📝 Generating text...")
        generate_text()

        print("🎙️ Generating voice...")
        generate_voice()

        print("📤 Sending to Telegram...")
        send_post()

        print("✅ Posting complete. Waiting 24h...")
    except Exception as e:
        print(f"❌ Error during cycle: {e}")

    # Ждём 24 часа
    time.sleep(86400)






