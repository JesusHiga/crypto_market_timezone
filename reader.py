
import pandas as pd
import numpy as np


def compil():
    dataframe = pd.DataFrame()    
    for i in range(18,23):
        df = pd.read_csv(f'/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_20{i}.csv',date_parser=True)
        dataframe = pd.concat([dataframe,df],ignore_index=True)
    dataframe = dataframe[['Date','Week_day','Market','Start','Finish','Open','Close','Change','Change_pct','Volume']]    
    print(dataframe)
        
    # return dataframe.to_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_total.csv',sep=',',encoding='utf-8',columns=['Date','Week_day','Market','Start','Finish','Open','Close','Change','Change_pct','Volume'],index=False)    
    return dataframe.to_json('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_total.json')
    
if __name__=='__main__':
    print(compil())    