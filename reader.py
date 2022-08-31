from unicodedata import numeric
import pandas as pd
import numpy as np


df = pd.read_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_frame_WS.csv', sep=',',dtype={'Open':np.float64,'Close':np.float64,'Change':np.float64},parse_dates=['Date'],encoding='utf-8',)
df = pd.DataFrame(df)

print(df)
print(df.info())
print(df.describe())
