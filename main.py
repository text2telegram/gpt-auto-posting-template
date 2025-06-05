
import os
from dotenv import load_dotenv

# Загружаем нужный .env-файл
env_file = os.getenv("ENV_FILE", ".env.smarttest")
load_dotenv(env_file)
print(f"✅ Loaded env: {env_file}")

# Импортируем функции
from generate_text import generate_text
from generate_voice import generate_voice
from send_to_telegram import send_post

if __name__ == "__main__":
    print("🚀 Starting content generation...")
    generate_text()
    generate_voice()
    send_post()
    print("✅ Post successfully sent!")




