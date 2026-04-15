import time

from scanner import scan_market
from brain import decide
from execution_engine import execute
from learning_engine import learn
from portfolio import portfolio
from telegram import send_message


# 🚀 START SYSTEM
print("🤖 HEDGE FUND AI V16 STARTED")

send_message("🚀 Hedge Fund AI V16 Started Successfully")


cycle = 0

while True:

    cycle += 1

    print(f"\n🔄 CYCLE {cycle}")

    # 📊 1. Scan Market
    signals = scan_market()

    if not signals:
        print("No signals found")
        time.sleep(10)
        continue


    # 🧠 2. Decide best trade
    trade = decide(signals)


    if trade:

        print(f"🔥 SIGNAL FOUND: {trade['symbol']} | SCORE: {trade['score']}")

        # 💰 3. Execute trade (simulation / paper trading)
        result = execute(trade, trade["price"])

        print(f"📊 EXECUTION RESULT: {result}")

        # 🧠 4. Learning system
        if result:
            learn(result)

        # 📲 5. Telegram notification
        send_message(
            f"📊 TRADE UPDATE\n"
            f"Symbol: {trade['symbol']}\n"
            f"Price: {trade['price']}\n"
            f"Result: {result}\n"
            f"Score: {trade['score']}"
        )

    else:
        print("⚠️ No high-quality trade selected")


    # 💼 6. Portfolio status
    send_message(
        f"💼 PORTFOLIO STATUS\n"
        f"Balance: {portfolio['balance']}\n"
        f"Open Positions: {len(portfolio['positions'])}\n"
        f"Cycle: {cycle}"
    )


    # ⏱️ Delay between scans
    time.sleep(15)
