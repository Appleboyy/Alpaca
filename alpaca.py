from alpaca_trade_api.rest import REST
api = REST()

api.get_bars("AAPL", TimeFrame.Hour, "2021-02-08", "2021-02-08", limit=10, adjustment='raw').df
x