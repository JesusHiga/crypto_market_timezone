from datetime import datetime
import tkinter

from pandas import to_datetime

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

if __name__ == '__main__':
    # y=[2019,2020,2021,2022,2023,2024,2025]
    # d=[10,8,14,13,12,10,9]
    # d2=[3,1,7,6,5,3,2]
    # for j,i in zip(y,d2) :   
    dt = datetime(2021,1,1,21,30,00)
    tempo = timestamp(dt)
    print(tempo)
    print(dt)
    a = 1648342800000
    print(to_datetime(a,unit='ms').date())
    print(to_datetime(a,unit='ms').time())
        
    # TKY 02:00, 07:30 
    # LND 08:00, 14:00 
    # NY 14:30, 20:30
    
    
    #enero
    # list_dict = [
    #             {'market':'tokyo',   'oh':1641002400000,'ch':1641022200000},
    #             {'market':'london',  'oh':1641024000000,'ch':1641045600000},
    #             {'market':'new_york','oh':1641047400000,'ch':1641069000000},
    #             ]
    
    
    # septiembre
    # list_dict = [
    #             {'market':'tokyo',   'oh':1661997600000,'ch':1662017400000},
    #             {'market':'london',  'oh':1662019200000,'ch':1662040800000},
    #             {'market':'new_york','oh':1662042600000,'ch':1662064200000},
    #             ]