import time
import requests
import ccxt
import pandas as pd

# =========================
# 📲 TELEGRAM
# =========================
TOKEN = "PUT_TOKEN"
CHAT_ID = "PUT_CHAT_ID"

def send_message(msg):
    if not TOKEN or not CHAT_ID:
        print(msg)
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass


# =========================
# ⚙️ EXCHANGE
# =========================
exchange = ccxt.kucoin({"enableRateLimit": True})
exchange.load_markets()

symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT"]


# =========================
# 💼 PORTFOLIO
# =========================
portfolio = {
    "balance": 1000,
    "positions": {},
    "closed": []
}

TRADE_SIZE = 100


# =========================
# 📊 DATA
# =========================
def get_data(symbol, tf="15m"):
    return pd.DataFrame(
        exchange.fetch_ohlcv(symbol, tf, limit=120),
        columns=["t","o","h","l","c","v"]
    )


# =========================
# 🌍 MULTI TF TREND
# =========================
def trend_ok(symbol):

    for tf in ["15
