
from environment import TradingEnv
from agent import Agent
from policy import update_q
from reward import get_reward
from scanner import get_state

def train():

    env = TradingEnv()
    agent = Agent()

    for episode in range(500):

        state = get_state()
        price = 100

        action = agent.act(state)

        reward = env.step(action, price)

        next_state = get_state()

        update_q(agent.q_table, str(state), action, reward)

    return agent
