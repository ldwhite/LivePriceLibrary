import pandas as pd
import time
from datetime import datetime
from yahoo_fin import stock_info as si
import csv

ticker = input("Enter desired ticker symbol: ")

price = si.get_live_price(f'{ticker}')
now = str(datetime.now())
data = {
    'Price':price
}

df = pd.DataFrame(data, index=[now])

if __name__ == "__main__":
    df.to_csv('data.csv')
    def save_data():
        with open(r'data.csv', 'a', newline = '') as csvfile:
            fieldnames = ['Time', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

            writer.writerow({'Time': now, 'Price': price})


    while True:
        now = str(datetime.now())
        price = si.get_live_price('AAPL')
        save_data()
        print(price)

        time.sleep(10)
