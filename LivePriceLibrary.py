import numpy as np
import pandas as pd
import time
from datetime import datetime
from datetime import time as dttime
from yahoo_fin import stock_info as si
import csv

if __name__ == "__main__":
    ticker = input("Enter desired ticker symbol: ")
    price = si.get_live_price(f'{ticker}')
    now = datetime.now()
    now_time = datetime.time(now)
    mkt_close = dttime(16, 0, 0)
    mkt_open = dttime(9, 30, 0)
    data = {
            'Price': price
        }

    def time_in_range(mkt_open, mkt_close, x):
        if mkt_close <= mkt_open:
            return mkt_close <= x <= mkt_open
        else:
            return mkt_close <= x or x <= mkt_open

    def save_data():
        with open(r'data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Time', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Time': now, 'Price': price})

    while True:
        if time_in_range(mkt_close, mkt_open, now_time):
            now = datetime.now()
            price = si.get_live_price('AAPL')
            save_data()
            print(price)
            time.sleep(10)
        else:
            pass
