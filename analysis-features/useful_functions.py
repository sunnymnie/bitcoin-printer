import numpy as np
from ta.trend import SMAIndicator

def log_abs(x, zeros=False):
    """
    returns ln(x), and -ln(abs(x)) if x is negative

    if zeros is True, returns 0 if abs(x)<1
    """
    # if zeros and abs(x)<1:
    #     return 0
    # return np.log(abs(x)) if x > 0 else -np.log(abs(x))

    return 0 if zeros and abs(x)<1 else np.log(abs(x)) if x > 0 else -np.log(abs(x))


def divide_none(x, y):
    """divides x and y, returns None if either are None"""
    if not isinstance(x, float) or not isinstance(y, float) or y == 0:
        return None
    else:
        return x/y

def none_subtraction(x, y):
    """
    returns x-y and None if either are None
    """
    if x is None or y is None:
        return None
    else:
        return x-y

def get_rate(x):
    """
    gets the rate of x
    """
    past = x.shift(1)
    return list(map(none_subtraction, x, past))

def get_moving_average(i, window:int):
    """
    returns the moving average of indicator i
    i: pandas series
    windows: [20, 50, 200]
    """
    sma = SMAIndicator(close=i, window=window)
    return sma.sma_indicator()


