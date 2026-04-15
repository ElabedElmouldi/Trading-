import random
import numpy as np

class Agent:

    def __init__(self):
        self.q_table = {}

    def get_state_key(self, state):
        return str(state)

    def act(self, state):

        if random.random() < 0.2:
            return random.choice([0,1,2])  # explore

        key = self.get_state_key(state)

        return self.q_table.get(key, 0)
