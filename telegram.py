import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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
