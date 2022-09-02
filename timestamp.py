from datetime import datetime

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000
if __name__ == '__main__':
    dt = datetime(2022,1,1,16,30,00)
    tempo = timestamp(dt)
    print(tempo)
    print(dt)