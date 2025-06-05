
import os
import time
from dotenv import load_dotenv
from generate_text import generate_text
from generate_voice import generate_voice
from send_to_telegram import send_post

env_file = os.getenv("ENV_FILE", ".env.smarttest")
load_dotenv(env_file)

print(f"✅ Loaded env: {env_file}")

while True:
    print("🚀 Starting new posting cycle...")
    generate_text()
    generate_voice()
    send_post()
    
    print("⏳ Waiting 24h for next post...")
    time.sleep(86400)  # 24 часа





