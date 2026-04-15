from trainer import train
from scanner import get_state

import random

print("🤖 HEDGE FUND AI V15 RL STARTED")

agent = train()

balance = 1000
position = None

while True:

    state = get_state()

    action = agent.act(state)

    price = 100 + random.uniform(-2,2)

    if action == 1:
        position = price

    elif action == 2 and position:
        profit = price - position
        balance += profit
        position = None

        print("💰 Trade closed | Profit:", profit)

    print("Balance:", balance)
