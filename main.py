import requests
from datetime import datetime

current_unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
past_unix_timestamp = (datetime(2023, 12, 1, 0, 0, 0) - datetime(1970, 1, 1)).total_seconds()

TARGET='RUB=X'
TIME1 = int(past_unix_timestamp)
TIME2 = int(current_unix_timestamp)

INTERVAL = '1d'
EVENT_TYPE = 'history'


URL = f'https://query1.finance.yahoo.com/v7/finance/download/{TARGET}?period1={TIME1}&period2={TIME2}&interval={INTERVAL}&events={EVENT_TYPE}&includeAdjustedClose=true'''

print(URL)
