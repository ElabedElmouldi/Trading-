
from strategy import score_asset

def scan_market(market):

    results = []

    for c in market:

        score = score_asset(c)

        if score >= 80:

            results.append({
                "symbol": c["symbol"],
                "price": c["price"],
                "score": score
            })

    return sorted(results, key=lambda x: x["score"], reverse=True)[:3]
