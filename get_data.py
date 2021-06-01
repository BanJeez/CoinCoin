import config

from binance.client import Client

#from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

#for price in prices:
   # print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

for candlestick in candles:
    print(candlestick)

print(len(candles))