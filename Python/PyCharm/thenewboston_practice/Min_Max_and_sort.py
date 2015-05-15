stocks = {
    'APPL': 230.34,
    'GOOG': 134.30,
    'AMZN': 430.32,
    'YHOO': 34.55,
    'FB': 39.00
}

print(min(zip(stocks.keys(),stocks.values())))

print(min(zip(stocks.values(),stocks.keys())))

print(max(zip(stocks.values(),stocks.keys())))

print(sorted(zip(stocks.values(),stocks.keys())))

print(sorted(zip(stocks.keys(),stocks.values())))
