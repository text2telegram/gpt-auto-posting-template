
import requests
import os

def generate_voice(text, voice="Rachel", filename="voice.mp3"):
    api_key = os.getenv("ELEVEN_API_KEY")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    json_data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    response = requests.post(url, headers=headers, json=json_data)
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename
