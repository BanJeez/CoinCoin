import config

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


client = Client(config.API_KEY, config.API_SECRET)