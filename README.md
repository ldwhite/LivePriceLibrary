# Live Market Data

<p align="center">
<img src = "https://github.com/ldwhite/Live_Market_Data/blob/main/images/stock_market.gif" style = "width:50%" />
</p>

This simple Python script continuously pulls the live market price of an equity from the exchange and adds it to a <code>.csv</code> file. While the way this script is currently set up is to merely add data to a file, this method has numerous applications: the script could easily be augmented to construct an automated trading bot, easily used in conjunction with my [pairs trading strategy](https://github.com/ldwhite/PairsTrading).

## Required Packages

<p align="center">
<img src = "https://github.com/ldwhite/Live_Market_Data/blob/main/images/packages.png" style = "width:50%" />
</p>

Whenever you're dealing with the DataFrame, the first package you'll want to load is <code>pandas</code>. Next, we load the <code>time</code> and <code>datetime</code> packages, as these will allow us to pull the time at which the live stock quote was gathered. Finally, we load the <code>yahoo_fin</code> package, which allows us to pull the live price of our desired stock as well as the <code>csv</code> package which allows us to continuously update the <code>.csv</code> file that is containing our stock prices.

## Setting up the Database

<p align="center">
<img src = "https://github.com/ldwhite/Live_Market_Data/blob/main/images/setup.png" style = "width:50%" />
</p>

To make this script easily implemented with the stock of your choice, the ticker is input by the user. Next, we create the <code>price</code> and <code>now</code> variables which will list our live stock data and time. We then construct a dictionary containing only the pricing data, which is then used to create our DataFrame, using the time at which the stock price was quoted as the index.

## Gathering the Live Data

<p align="center">
<img src = "https://github.com/ldwhite/Live_Market_Data/blob/main/images/execution.png" style = "width:50%" />
</p>

We then export the DataFrame to a <code>.csv</code> file and create a function called <code>save_data()</code> which appends the existing <code>.csv</code> file with the new stock price. We then continuously pull the live stock price, calling our <code>save_data()</code> function to add this new data to our <code>.csv</code> file, and specify that we want the price quotes to be pulled every 10 seconds with <code>time.sleep(10)</code>.
