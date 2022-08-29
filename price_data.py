from pprint import pprint
from binance.spot import Spot
from numpy import inner, nan_to_num
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
        
    
    def zoneh(self,x, limit: int = 1):
        data_frame = pd.DataFrame(columns=['Open time','Close time','Open','High','Low','Close','Volume','Open_time','Close_time'])
        for i in range(x):
            df = pd.DataFrame(self.binance_client().klines(symbol=self.pair, interval=self.temporality,limit=limit,startTime=1641047400000+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
            df = df[['Open time','Close time','Open','High','Low','Close','Volume']]
            df['Open_time'] = pd.to_datetime(df['Open time'],unit='ms')
            df['Close_time'] = pd.to_datetime(df['Close time'],unit='ms')
            data_frame = pd.concat([data_frame,df],ignore_index=True)
        data_frame['Date'] = data_frame['Open_time'].dt.strftime(('%d-%m-%Y'))
        data_frame['Week_day'] = pd.to_datetime(data_frame['Open time'],unit='ms',utc=False).dt.day_name()
        data_frame = data_frame.drop(['Open time','Close time','Open_time','Close_time'],axis=1)    
        data_frame = data_frame[['Date','Week_day','Open','High','Low','Close','Volume']]
        data_frame['Change'] = [(data_frame['Open'].values[i]/data_frame['Open'].values[i-1])-1 for i in range(len(data_frame))]
        pprint(data_frame)
        data_frame.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_frame.csv',sep=',')        
        
        #https://datascientyst.com/convert-datetime-day-of-week-name-number-in-pandas/
    
    def market_time(self,x,limit: int=1):
        date = pd.DataFrame(columns=['Date'])
        open = pd.DataFrame(columns=['Open'])
        close = pd.DataFrame(columns=['Close'])
        day = pd.DataFrame(columns=['Week_day'])
        for i in range(x):
            df_open = pd.DataFrame(self.binance_client().klines(symbol=self.pair, interval=self.temporality, limit=limit, startTime=1641047400000+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
            df_open['Date'] = pd.to_datetime(df_open['Open time'],unit='ms').dt.strftime(('%d-%m-%Y')) 
            df_day = df_open[['Open time']]
            df_date = df_open[['Date']] 
            df_open = df_open[['Open']]
            df_close = pd.DataFrame(self.binance_client().klines(symbol=self.pair, interval=self.temporality, limit=limit, startTime=1641069000000+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
            df_close = df_close[['Close']]
            date = pd.concat([date,df_date], ignore_index=True)
            open = pd.concat([open,df_open], ignore_index=True)
            close = pd.concat([close,df_close], ignore_index=True)
            day = pd.concat([day,df_day], ignore_index=True)
        data_frame = pd.concat([date,open,close,day],axis=1)
        data_frame['Week_day'] = pd.to_datetime(data_frame['Open time'],unit='ms',utc=False).dt.day_name()
        data_frame['Change'] = data_frame['Close']/data_frame['Open']-1
        data_frame = data_frame[['Date','Week_day','Open','Close','Change']]
        data_frame['Open'] = data_frame['Open'].astype(float)
        data_frame['Close'] = data_frame['Close'].astype(float)
        data_frame['Change'] = data_frame['Change'].astype(float)
        
        print(data_frame) 
        data_frame.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_frame_WS.csv',sep=',')        
        
bot = robo_binance('btcusdt', '30m')
pprint(bot.market_time(3))


    

    # if __name__=="__main__":
    #     print(candlestick('BTCBUSD'))
