import random

def get_state():

    return {
        "trend": random.choice([0,1]),
        "momentum": random.uniform(-1,1),
        "volume": random.uniform(0,2)
    }
