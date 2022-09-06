from pprint import pprint
from binance.spot import Spot
from numpy import empty
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
    
    def market_time(self,x,limit: int=1) -> pd.DataFrame :
        
        """nuevas dataframes, listas para concatenar"""  
        date = pd.DataFrame(columns=['Date'])
        market = pd.DataFrame(columns=['market'])
        open = pd.DataFrame(columns=['Open'])
        close = pd.DataFrame(columns=['Close'])
        day = pd.DataFrame(columns=['Open time'])
        finish = pd.DataFrame(columns=['Finish'])
        
        """for loop para agregar dias al dataframe"""
        for i in range(x):
            
            list_dict = [
                {'market':'tokyo',   'oh':1661997600000,'ch':1662017400000},
                {'market':'london',  'oh':1662019200000,'ch':1662040800000},
                {'market':'new_york','oh':1662042600000,'ch':1662064200000},
                ]
                
            for j in range(len(list_dict)):
                
                df_open = pd.DataFrame(self.binance_client().klines(symbol=self.pair, interval=self.temporality, limit=limit, startTime=list_dict[j]['oh']+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
                df_open['Date'] = pd.to_datetime(df_open['Open time'],unit='ms').dt.strftime(('%Y-%m-%d'))     
                df_day = df_open[['Open time']]
                df_date = df_open[['Date']] 
                df_open1 = df_open[['Open']]
                df_market = pd.DataFrame(list_dict[j],columns=['market'],index=[0])
                
                #Dataframe diferente para definir la hora de cierre
                df_close = pd.DataFrame(self.binance_client().klines(symbol=self.pair, interval=self.temporality, limit=limit, startTime=list_dict[j]['ch']+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
                df_close1 = df_close[['Close']]
                df_close['Finish'] = pd.to_datetime(df_close['Close time'],unit='ms').dt.strftime(('%H:%M:%S')) 
                df_close2 = df_close[['Finish']]
                
                #Concatenamos los dataframes induvidualmente con los nuevos
                date = pd.concat([date,df_date], ignore_index=True)
                market = pd.concat([market,df_market], ignore_index=True)
                open = pd.concat([open,df_open1], ignore_index=True)
                close = pd.concat([close,df_close1], ignore_index=True)
                day = pd.concat([day,df_day], ignore_index=True)
                finish = pd.concat([finish,df_close2], ignore_index=True)
                
                #Mostramos los precios de cierre en pantalla
                print(df_close1)
                       
        #concatenamos todos los dataframes en uno solo    
        data_frame = pd.concat([date,market,open,close,day,finish],axis=1)
        
        #agregamos columnas, week_day y change
        data_frame['Week_day'] = pd.to_datetime(data_frame['Open time'],unit='ms',utc=False).dt.day_name()
        data_frame['Change'] = data_frame['Close']/data_frame['Open']-1
        data_frame['start'] = pd.to_datetime(data_frame['Open time'],unit='ms').dt.strftime(('%H:%M:%S')) 
        # data_frame['finish'] = pd.to_datetime(df_close['Close time'],unit='ms').dt.strftime(('%H:%M:%S')) 
        
        #ordenamos las columnas
        data_frame1 = data_frame[['Date','market','Week_day','start','Finish','Open','Close','Change']]
        #convertimos en float las columnas de datos numericos
        data_frame1['Open'] = data_frame1['Open'].astype(float)
        data_frame1['Close'] = data_frame1['Close'].astype(float)
        data_frame1['Change'] = data_frame1['Change'].astype(float)
        
        #imprimimos y guardamos el resultado final
        print(data_frame1) 
        data_frame.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_frame.csv',sep=',')        
        
bot = robo_binance('btcusdt', '30m')
pprint(bot.market_time(6))


    

  
