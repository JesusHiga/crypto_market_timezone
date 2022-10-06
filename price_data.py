from binance.spot import Spot
import config
import pandas as pd
import json
import datetime


class robo_binance:
    
    __api_key = config.API_KEY
    __api_secret = config.API_SECRET_KEY
    
    # client = Spot(key = config.API_KEY, secret = config.API_SECRET_KEY)

    def __init__(self, pair: str, temporality: str):
        self.pair = pair.upper()
        self.temporality = temporality
        self.symbol = self.pair.removeprefix('USDT')
        
    def binance_client(self):
        """
        Inicia la conexion de binance con el mercado spot
        """        
        return Spot(key=self.__api_key, secret=self.__api_secret)
    
    def binance_account(self) -> dict:
        
        return self.binance_client().account()
    
    def cryptocurrencies(self) -> list[dict]:
        """
        Devuelve una lista de  todas las cryptomonedas que tengan un saldo positivo
        """
        return [crypto for crypto in self.binance_account().get('balances') if float(crypto.get('free')) > 0]
    
    def symbol_price(self, pair: str = None):
        """
        Devuelve el precio para determinado par
        """
        pair = self.pair if pair is None else pair
        
        return float(self.binance_client().ticker_price(pair.upper()).get('price')) 
    

    def candlestick(self,limit: int = 1) -> pd.DataFrame:
        candle = pd.DataFrame(self.binance_client().klines(symbol=self.pair,interval=self.temporality,limit=limit,startTime=1641043800000   ), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)
        candle = candle[['Open time','Close time','Open','High','Low','Close','Volume']]
        candle['Open_time'] = pd.to_datetime(candle['Open time'],unit='ms')
        candle['Close_time'] = pd.to_datetime(candle['Close time'],unit='ms')
        # candle = candle.drop(columns=['Open time','Close time'])
        candle.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data.csv',sep=',')
        return candle    
    

bot = robo_binance('btcusdt', '30m')



