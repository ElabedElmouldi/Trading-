import ccxt

exchange = ccxt.binance()

def get_symbols():
    markets = exchange.load_markets()
    return [s for s in markets if "/USDT" in s][:80]


def get_price(symbol):
    return exchange.fetch_ticker(symbol)["last"]
