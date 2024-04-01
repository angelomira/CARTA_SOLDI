import time

i = 0

# для ежесекундной проверки (realtime значения)
while True:
    import yfinance as yf
    msft = yf.Ticker('RUB=X')
    
    print(msft.history(period='1d', interval='1m').iloc[-1])
    i += 1
    print(i // 9)
    time.sleep(1)