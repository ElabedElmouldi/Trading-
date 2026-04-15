class TradingEnv:

    def __init__(self):
        self.balance = 1000
        self.position = None

    def step(self, action, price):

        reward = 0

        # BUY
        if action == 1 and self.position is None:
            self.position = price

        # SELL
        elif action == 2 and self.position is not None:

            reward = price - self.position
            self.balance += reward
            self.position = None

        # HOLD
        return reward
