
# Risk analysis of Stocks
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as pyplot

# all libraries are imported

stocks = yf.download(['MSFT' , 'TSLA'], start="2018-01-01" , end="2022-02-01")
#data source from two providers microsoft and Tesla - these companies store data , google them
# entire data set downloaded for the specified dates

stocksData = stocks.loc[:,"Close"].copy()
#we are taking close column separately - analysis is based on closing price of the stock
stocksData.head(5)

stocksData.plot(figsize = (20,10), fontsize=15)
pyplot.style.use("classic")
pyplot.show()
#plot shows how the price variation happened in few years

#calculate %change - NaN values- no data vale- may be no trdae happened on that day
data = stocksData.pct_change().dropna()
print(data)
data = data.describe() #gives alll details
data = data.describe().T.loc[:,["mean", "std"]]
print(data)
# these values are only for a single day. we have to calculate it for the whole year and we guess that there are 251 trading days


data["mean"] = data["mean"]*251
data["std"] = data["std"] * np.sqrt(251)
print(data)

# scatter plot x axis is std dev and y axis is mean
data.plot.scatter(figsize= (20,10), fontsize=15, x="std", y= "mean")
for idx in data.index:
    pyplot.annotate(idx, xy=(data.loc[idx, "std"] + 0.005, data.loc[idx, "mean"] + 0.005))
pyplot.show()

# second graph shows the way tesla stocks have taken high risk from 2018 to 2022, deviation, mean is high and you can gain more profit with high risk


