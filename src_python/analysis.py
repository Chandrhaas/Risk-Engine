import pandas as pd
import numpy as np
import os

def calculate_parameters(prices: pd.DataFrame):

    #returns = log(a t/ a t-1) , we take log beacause it is addidtive over time and addition is faster than multiplication
    returns = np.log(prices/prices.shift(1)).dropna()

    trading_days=252

    mean_s= returns.mean()*trading_days

    cov_s=returns.cov()*trading_days

    return mean_s.to_numpy(), cov_s.to_numpy()