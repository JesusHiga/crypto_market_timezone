from ast import Return
from posixpath import split
import pandas as pd
import json

# df = pd.read_csv('/Users/macbook/platzi/web_scraping_03/binance_bot/scripts/data.csv', orient=split,precise_float=True)
# print()


# def ox(x):   
#     df = pd.DataFrame({'a':[]}) 
#     for i in range(11):
#         # df1 = pd.DataFrame({'a':[1,2,3]}) 
#         df2 = pd.DataFrame({'a':[4+i,5+i,6+i]})
#         df = pd.concat([df,df2],ignore_index=True)
#     print(df)

# # ab = pd.DataFrame()
# # print(ab)
# if __name__=="__main__":
#     ox(5)


list_dict = [{'market':'new_york','oh':1641047400000,'ch':1641069000000},{'market':'london','oh':1641024000000,'ch':1641052800000},{'market':'tokyo','oh':1640995200000,'ch':1641015000000}]
# list_dict = [{'new_york':1641047400000,'london':1641024000000,'tokyo':1640995200000}]
# list_dict2 = [{'new_york_close':1641069000000,'london_close':1641052800000,'tokyo_close':1641015000000}]

df = pd.DataFrame(columns=['market'])
for i in range(len(list_dict)):
    
    df_market = pd.DataFrame(list_dict[i],columns=['market'],index=[0])
    df = pd.concat([df,df_market], ignore_index=True)
print(df)
    