from unicodedata import numeric
import pandas as pd
import numpy as np


# df = pd.read_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/files/data_frame_NY.csv', sep=',',dtype={'Open':np.float64,'Close':np.float64,'Change':np.float64},parse_dates=['Date'],encoding='utf-8',)
# df = pd.DataFrame(df)

# print(df)
# print(df.info())
# print(df.describe())


list_dict = [
                {'market':'tokyo',   'oh':1641002400000,'ch':1641022200000},
                {'market':'london',  'oh':1648263600000,'ch':1651028400000},
                {'market':'new_york','oh':1641047400000,'ch':1641069000000},
                ]

print(list_dict[0]['market'])
