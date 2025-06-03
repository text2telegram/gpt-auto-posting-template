
from openai import OpenAI
import os
from dotenv import load_dotenv
from send_to_telegram import send_post
from generate_text import generate_hook, generate_lesson
from generate_voice import generate_voice

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if __name__ == "__main__":
    print("Bot is running...")
    hook = generate_hook()
    lesson = generate_lesson()
    audio_path = generate_voice(lesson)
    send_post(hook, lesson, audio_path)

