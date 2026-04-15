weights = {
    "trend": 1.0,
    "volume": 1.0,
    "momentum": 1.0
}

def learn(result):

    if result == "WIN":
        weights["momentum"] += 0.01
    else:
        weights["volume"] -= 0.01
