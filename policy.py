def update_q(q_table, state, action, reward, alpha=0.1):

    if state not in q_table:
        q_table[state] = 0

    q_table[state] += alpha * (reward - q_table[state])
