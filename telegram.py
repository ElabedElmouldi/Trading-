import os, requests

def send(msg):

    token = os.getenv("BOT_TOKEN")
    chat = os.getenv("CHAT_ID")

    if not token or not chat:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat,
        "text": msg
    })
