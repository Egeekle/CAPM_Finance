##create cluster model
##create cluster model 

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['TSLA','^GSPC']

data = pd.DataFrame()
for t in tickers:
    data[t] = yf.Ticker(tickers)

log_returns = np.log(1 + data.pct_change())
cov = log_returns.cov()*252

cov_with_market = cov.iloc[0,1]
market_var = log_returns['^GSPC'].var()*252
stock_beta = cov_with_market / market_var

riskfree = 0.0095
riskpremium = (log_returns['^GSPC'].mean()*252) - riskfree

stock_capm_return = riskfree + stock_beta * riskpremium
sharpe_stock = (stock_capm_return - riskfree) /(log_returns['TSLA'].std()*252**0.5)

print("La Beta de " + str(tickers) + " es de: " + str(round(stock_beta,3)))
print("El retorno CAPM de " + str(tickers) + " es de: " + str(round(stock_capm_return*100,3))+"%")
print("El Ratio Sharpe de " + str(tickers) + " es de: " + str(round(sharpe_stock,3)))
