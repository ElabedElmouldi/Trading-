
def decide(trades):

    if not trades:
        return None

    best = max(trades, key=lambda x: x["score"])

    if best["score"] < 85:
        return None

    return best
