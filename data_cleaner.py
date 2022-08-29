from ast import Return
from posixpath import split
import pandas as pd
import json

# df = pd.read_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/data.csv', orient=split,precise_float=True)
# print()


def ox(x):   
    df = pd.DataFrame({'a':[]}) 
    for i in range(11):
        # df1 = pd.DataFrame({'a':[1,2,3]}) 
        df2 = pd.DataFrame({'a':[4+i,5+i,6+i]})
        df = pd.concat([df,df2],ignore_index=True)
    print(df)

# ab = pd.DataFrame()
# print(ab)
if __name__=="__main__":
    ox(5)