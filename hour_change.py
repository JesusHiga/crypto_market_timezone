
from datetime import datetime, timedelta
import pandas as pd


mhours = [
        {'market':'tokyo','year':2018,'summer':0000000000000, 'winter': 0000000000000,'oh':1514772000000,'ch':1514791800000,'difh':19800000},
        # {'market':'tokyo','year':2019,'summer':0000000000000, 'winter': 0000000000000,'oh':1546308000000,'ch':1546327800000,'difh':19800000},
        # {'market':'tokyo','year':2020,'summer':0000000000000, 'winter': 0000000000000,'oh':1577844000000,'ch':1577863800000,'difh':19800000},
        # {'market':'tokyo','year':2021,'summer':0000000000000, 'winter': 0000000000000,'oh':1609466400000,'ch':1609486200000,'difh':19800000},
        # {'market':'tokyo','year':2022,'summer':0000000000000, 'winter': 0000000000000,'oh':1641002400000,'ch':1641022200000,'difh':19800000},
#         {'market':'tokyo','year':2023,'summer':0000000000000, 'winter': 0000000000000},
#         {'market':'tokyo','year':2024,'summer':0000000000000, 'winter': 0000000000000},
#         {'market':'tokyo','year':2025,'summer':0000000000000, 'winter': 0000000000000},
        
        {'market':'london','year':2018,'summer':1521939600000, 'winter': 1540692000000,'oh':1514793600000,'ch':1514815200000,'difh':21600000},
        # {'market':'london','year':2019,'summer':1553994000000, 'winter': 1572141600000,'oh':1546329600000,'ch':1546351200000,'difh':21600000},
        # {'market':'london','year':2020,'summer':1585443600000, 'winter': 1603591200000,'oh':1577865600000,'ch':1577887200000,'difh':21600000},
        # {'market':'london','year':2021,'summer':1616893200000, 'winter': 1635645600000,'oh':1609488000000,'ch':1609509600000,'difh':21600000},
        # {'market':'london','year':2022,'summer':1648342800000, 'winter': 1667095200000,'oh':1641024000000,'ch':1641045600000,'difh':21600000},
        
        # {'market':'london','year':2023,'summer':1679792400000, 'winter': 1698544800000},
        # {'market':'london','year':2024,'summer':1711846800000, 'winter': 1729994400000},
        # {'market':'london','year':2025,'summer':1743296400000, 'winter': 1761444000000},
        
       


          {'market':'new_york','year':2018,'summer':1520733600000, 'winter': 1541296800000,'oh':1514817000000,'ch':1514838600000,'difh':21600000},
        # {'market':'new_york','year':2019,'summer':1552183200000, 'winter': 1572746400000,'oh':1546353000000,'ch':1546374600000,'difh':21600000},
        # {'market':'new_york','year':2020,'summer':1583632800000, 'winter': 1604196000000,'oh':1577889000000,'ch':1577910600000,'difh':21600000},
        # {'market':'new_york','year':2021,'summer':1615687200000, 'winter': 1636250400000,'oh':1609511400000,'ch':1609533000000,'difh':21600000},
        # {'market':'new_york','year':2022,'summer':1647136800000, 'winter': 1667700000000,'oh':1641047400000,'ch':1641069000000,'difh':21600000},
        
#         {'market':'new_york','year':2023,'summer':1678586400000, 'winter': 1699149600000},
#         {'market':'new_york','year':2024,'summer':1710036000000, 'winter': 1730599200000},
#         {'market':'new_york','year':2025,'summer':1741485600000, 'winter': 1762048800000},        

 ]

#https://www.hora.co/cambiohorario/dst.do?tz=Europe/London

# ldn = [{'year':2019,'summer':[3,31], 'winter': '10-27'},
#     {'year':2020,'summer':[3,29], 'winter': '10-25'},
#     {'year':2021,'summer':[3,28], 'winter': '10-31'},
#     {'year':2022,'summer':[3,27], 'winter': '10-30'},
#     {'year':2023,'summer':[3,26], 'winter': '10-29'},
#     {'year':2024,'summer':[3,31], 'winter': '10-27'},
#     {'year':2025,'summer':[3,30], 'winter': '10-26'},]

# #https://www.hora.co/cambiohorario/dst.do?tz=America/New_York

# ny = [{'year':2019,'summer':[3,10], 'winter': '11-3'},
#     {'year':2020,'summer':[3,8], 'winter': '11-1'},
#     {'year':2021,'summer':[3,14], 'winter': '11-7'},
#     {'year':2022,'summer':[3,13], 'winter': '11-6'},
#     {'year':2023,'summer':[3,12], 'winter': '11-5'},
#     {'year':2024,'summer':[3,10], 'winter': '11-3'},
#     {'year':2025,'summer':[3,9], 'winter': '11-2'},]


# def zt(place,y):
#     dt = datetime(ldn[y]['year'], 
#                   ldn[y]['summer'][0], 
#                   ldn[y]['summer'][1], 
#                   3, tzinfo=ZoneInfo(place))
#     return dt, dt.tzname()
    
# if __name__=='__main__':
#     # print(zt("AMERICA/NEW_YORK",4)) 
#     print(zt("EUROPE/LONDON",0))    



# def hourinfo():
#     dt = datetime(2019,3,31,1, tzinfo=ZoneInfo("EUROPE/LONDON"))
#     print(dt)
#     print(dt.tzname())
#     print(timedelta(days=2))
#     print(dt + timedelta(days=2))
#     print(dt.replace(fold=1).astimezone().time())
    
# if __name__=='__main__':
#     hour = hourinfo()
#     print(hour)  
#     print(len(mhours))  
#     a = [mhours[i]['summer'] for i in range(len(mhours))]
#     print(a)
    
