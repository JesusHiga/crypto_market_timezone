import numpy as np
import hour_change
import price_data as priced
import pandas as pd
from datetime import datetime
from numba import njit

# list_dict = [
#                 {'market':'tokyo',   'oh':1641002400000,'ch':1641022200000},
#                 {'market':'london',  'oh':1641024000000,'ch':1641045600000},
#                 {'market':'new_york','oh':1641047400000,'ch':1641069000000},
#                 ]

def dfdate(self,x,limit: int=1) -> pd.DataFrame :
    date = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality, limit=limit, startTime=hour_change.mhours[j]['oh']+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float) 
            df1 = df.copy()
            df1['Date'] = pd.to_datetime(df['Open time'],unit='ms').dt.strftime(('%Y-%m-%d'))
            print(df1)
            date = pd.concat([date,df1], ignore_index=True)  
    date = date[['Date']]                  
    return date


def dfday(self,x,limit: int=1) -> pd.DataFrame :
    day = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=hour_change.mhours[j]['oh']+86400000*i), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)
            df1 = df[['Open time']].copy()
            print(df1)
            day = pd.concat([day,df1], ignore_index=True)
    day['Week_day'] = pd.to_datetime(day['Open time'], unit='ms', utc=False).dt.day_name()
    day = day[['Week_day']]
    return day

  
def dfmarket(self,x,limit: int=1) -> pd.DataFrame :
    market = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            df = pd.DataFrame(hour_change.mhours[j], columns=['market'], index=[0])
            df1 = df.copy()
            print(df1)
            market = pd.concat([market,df1], ignore_index=True)
    market['Market'] = market['market']
    market = market[['Market']]
    return market    
    
            
def dfstart(self,x,year,limit: int=1) -> pd.DataFrame :
    start = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            a = hour_change.mhours[j]['oh']+86400000*i
            year = hour_change.mhours[j]['year'] 
            summer = hour_change.mhours[j]['summer']
            winter = hour_change.mhours[j]['winter']
            b = a + 3600000 if a >= summer and a < winter else a if year == year else a   
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=b), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)    
            df = df[['Open time']].copy()
            print(df)
            start = pd.concat([start,df], ignore_index=True) 
    start['Start'] = pd.to_datetime(start['Open time'],unit='ms').dt.strftime('%H:%M:%S')
    start = start[['Start']]        
    return start    
    
    
def dffinish(self,x,year,limit: int=1) -> pd.DataFrame :
    finish = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            a = hour_change.mhours[j]['ch']+86400000*i
            year = hour_change.mhours[j]['year'] 
            summer = hour_change.mhours[j]['summer']
            winter = hour_change.mhours[j]['winter']
            b = a + 3600000 if a >= summer and a < winter else a if year == year else a   
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=b), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)    
            df = df[['Close time']].copy()
            print(df)
            finish = pd.concat([finish,df], ignore_index=True)         
    finish['Finish'] = pd.to_datetime(finish['Close time'],unit='ms').dt.strftime('%H:%M:%S')
    finish = finish[['Finish']]        
    return finish  


def dfopen(self,x,year,limit: int=1) -> pd.DataFrame :
    open = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            a = hour_change.mhours[j]['oh']+86400000*i
            year = hour_change.mhours[j]['year'] 
            summer = hour_change.mhours[j]['summer']
            winter = hour_change.mhours[j]['winter']
            b = a + 3600000 if a >= summer and a < winter else a if year == year else a   
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=b), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)    
            df = df[['Open']].copy()
            print(df)
            open = pd.concat([open,df], ignore_index=True)
    open =  open[['Open']].astype(float)
    return open


def dfclose(self,x,year,limit: int=1) -> pd.DataFrame :
    close = pd.DataFrame()
    for i in range(x):
        for j in range(len(hour_change.mhours)):
            a = hour_change.mhours[j]['ch']+86400000*i
            year = hour_change.mhours[j]['year'] 
            summer = hour_change.mhours[j]['summer']
            winter = hour_change.mhours[j]['winter']
            b = a + 3600000 if a >= summer and a < winter else a if year == year else a   
            df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=b), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)    
            df = df[['Close']].copy()
            print(df)
            close = pd.concat([close,df], ignore_index=True)
    close =  close[['Close']].astype(float)
    return close

# def dos(function):
#     def wrapper(*args):
#         initial = datetime.now()
#         function(*args)
#         final = datetime.now()
#         elapsed = final - initial
#         print(str(elapsed.total_seconds())+' seconds')        
#     return wrapper

def dfvolume(self,x,year,limit: int=1) -> pd.DataFrame :
    volume = pd.DataFrame()
    
    for i in range(x):
        volume_day = pd.DataFrame()
        for k in range(12):
            volume_h = pd.DataFrame()
            for j in range(len(hour_change.mhours)):
                a = hour_change.mhours[j]['oh']+86400000*i
                year = hour_change.mhours[j]['year'] 
                summer = hour_change.mhours[j]['summer']
                winter = hour_change.mhours[j]['winter']
                # while (hour_change.mhours[j]['ch']+86400000*i) - (hour_change.mhours[j]['oh']+86400000*i) <= hour_change.mhours[j]['difh']:
                
                b = a + 3600000 if a >= summer and a < winter else a if year == year else a   
                df = pd.DataFrame(priced.bot.binance_client().klines(symbol=priced.bot.pair, interval=priced.bot.temporality,limit=limit, startTime=b+k*18000000), columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'],dtype=float)    
                df1 = df[['Volume']].copy()
                volume_h = pd.concat([volume_h,df1],ignore_index=True,axis=1)
                print(volume_h)
            volume_day = pd.concat([volume_day,volume_h],ignore_index=True)
            volume_day1 = volume_day.T
        volume = pd.concat([volume,volume_day1],ignore_index=True)    
        volume =  volume.astype(float)   
    volume['Volume'] = volume.sum(axis=1)  
    volume = volume[['Volume']]  
    return volume

    
if __name__=='__main__':
        
    n = 365
    year = 2018
    data_name = f'data_{year}'

    date = dfdate(priced.bot.pair,n).to_dict()
    day = dfday(priced.bot.pair,n).to_dict()
    market = dfmarket(priced.bot.pair,n).to_dict()
    start = dfstart(priced.bot.pair,n,year).to_dict()
    finish = dffinish(priced.bot.pair,n,year).to_dict()
    open = dfopen(priced.bot.pair,n,year).to_dict()
    close = dfclose(priced.bot.pair,n,year).to_dict()
    volume = dfvolume(priced.bot.pair,n,year)
    
    list_dict_result = [date,day,market,start,finish,open,close,volume]
    
    def main():
        # data = pd.DataFrame()
        df = pd.concat(map(pd.DataFrame,list_dict_result),axis=1).dropna()
        df['Change'] = df['Close'] - df['Open']
        df['Change_pct'] = df['Close']/df['Open']-1
        df = df[['Date','Week_day','Market','Start','Finish','Open','Close','Change','Change_pct','Volume']]
        df.to_csv(f'/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/{data_name}.csv',sep=',')    
        return df
    
    print(main())
    
    # print(market)
