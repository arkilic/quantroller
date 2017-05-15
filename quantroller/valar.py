"""This file provides the API to calculate stock alpha, beta, chi^2 using statmodels"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from pandas_datareader.data import DataReader


start_dt = "2008-1-1"
equity_sym = ['SPY', 'AAPL', 'BP'] 

def compose_dataframe(equity_sym):
    """Provided a list of stock symbols, return a dataframe for Adj close """
    df = pd.DataFrame() # init empty dframe

    for s in equity_sym:
        tmp = DataReader(s, "yahoo", start_dt) # yahoo stands for source, not equity
        df[s] = tmp['Adj Close']
    return df


def resample(df, samp_type='M'):
    """Resample the data from daily to monthly """
    return df.resample(samp_type).last()


def vis_data(dfmret, alpha=0.7, color='blue', symbol=None):
    fig, ax1 = plt.subplots(1,figsize=(15,6))
    ax1.scatter(dfmret[symbol],dfmret.iloc[:,0],label="monthly returns",
                color=color, edgecolors='none', alpha=alpha)
    ax1.grid(True)

    ax1.set_xlabel("S&P500 Monthly Returns")
    ax1.set_ylabel("%s Monthly Returns" % (dfmret.columns[0]))
    plt.show()


def fit(X, y):
    """Fit data using Ordinary Least Squares """
    # TODO: Extend this to other methods
    model = sm.OLS(y, X).fit()
    return model


def model_summary(model):
    return model.summary()
