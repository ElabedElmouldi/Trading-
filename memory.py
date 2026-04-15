memory = []

def store(state, action, reward, next_state):
    memory.append((state, action, reward, next_state))
