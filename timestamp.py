from datetime import datetime
import tkinter

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000
if __name__ == '__main__':
    dt = datetime(2022,9,1,8,00,00)
    tempo = timestamp(dt)
    print(tempo)
    print(dt)
    
    # NY 14:30, 20:30
    # LND 08:00, 14:00 
    # TKY 02:00, 07:30 