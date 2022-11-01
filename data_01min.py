import numpy as np
import hour_change
import price_data as priced
import pandas as pd
from datetime import datetime

startday = 1662042600000 # 2022-09-01 14:30:00
minrange = 900000 # 60000 1min
ndays = 60

def dfdate(self,x,limit: int=1) -> pd.DataFrame :
    date = pd.DataFrame()
    for j in range(ndays):
        for i in range(x):
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality, limit=limit, startTime=(startday+j*86400000)+minrange*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
            df1 = df.copy()
            df1['Date'] = pd.to_datetime(df['Open time'],unit='ms').dt.strftime(('%Y-%m-%d-%H:%M:%S'))
            date = pd.concat([date,df1], ignore_index=True)  
    date = date[['Date']]                  
    return date

def dfprice(self,x,limit: int=1) -> pd.DataFrame :
    price = pd.DataFrame()
    for j in range(ndays):
        for i in range(x):
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality, limit=limit, startTime=(startday+j*86400000)+minrange*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)
            df1 = df.copy()
            df1 = df1[['Open','High','Low','Close','Volume']]
            price = pd.concat([price,df1], ignore_index=True)
    return price

if __name__ == '__main__':

    n = 25
    date = dfdate(priced.bot.pair,n).to_dict()
    price = dfprice(priced.bot.pair,n).to_dict()
    
    list_dict = [date,price]
    
    def main():
        for i in range(ndays):
            df = pd.concat(map(pd.DataFrame,list_dict),axis=1).dropna()
            return df
        
    print(main())
    data = main()
    data.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_01min.csv',sep=',')    