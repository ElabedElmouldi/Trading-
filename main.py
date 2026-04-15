import time
from data_feed import get_symbols, get_price
from scanner import scan_market
from brain import decide
from execution_engine import execute
from learning_engine import learn

print("🤖 HEDGE FUND AI V12 STARTED")

def fake_market():

    import random

    coins = []

    for i in range(80):

        coins.append({
            "symbol": f"COIN{i}/USDT",
            "price": 100,
            "trend_5m": random.choice(["UP","DOWN"]),
            "trend_1h": random.choice(["UP","DOWN"]),
            "volume": random.uniform(1,2),
            "momentum": random.uniform(1,2),
            "volatility": random.uniform(0.8,2),
            "near_resistance": random.choice([True,False])
        })

    return coins


while True:

    market = fake_market()

    signals = scan_market(market)

    trade = decide(signals)

    if trade:

        price = trade["price"]

        result = execute(trade, price)

        if result in ["TP", "SL"]:
            learn("WIN" if result == "TP" else "LOSS")

    print("Cycle complete...")

    time.sleep(10)
