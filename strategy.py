def score_asset(c):

    score = 0

    if c["trend_5m"] == "UP" and c["trend_1h"] == "UP":
        score += 30

    if c["volume"] > 1.7:
        score += 20

    if c["momentum"] > 1.5:
        score += 20

    if c["volatility"] < 1.5:
        score += 15

    if c["near_resistance"]:
        score += 15

    return score
