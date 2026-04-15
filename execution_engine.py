
positions = {}

def execute(trade, price):

    symbol = trade["symbol"]

    if symbol not in positions:

        positions[symbol] = {
            "entry": price,
            "tp": price * 1.05,
            "sl": price * 0.98
        }

        return "OPEN"

    pos = positions[symbol]

    if price >= pos["tp"]:
        del positions[symbol]
        return "TP"

    if price <= pos["sl"]:
        del positions[symbol]
        return "SL"

    return None
