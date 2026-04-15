import os
import requests

TOKEN = os.getenv(" 8439548325:AAHOBBHy7EwcX3J5neIaf6iJuSjyGJCuZ68")
CHAT_ID = os.getenv("5067771509")

def send_message(text):

    if not TOKEN or not CHAT_ID:
        print("⚠️ Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        })
    except Exception as e:
        print("Telegram error:", e)
