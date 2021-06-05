import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ta.trend import SMAIndicator
import useful_functions as uf


# def get_wr_target(df_close: list[float], span: int, limit):
#     """returns weighted range target given df['close']. Use limit=False to not
#     classify, else float"""
#     acc = []
#     df_len = len(df_close)

#     for i in range(len(df_close)):

#         if i+span < df_len:
#             close = df_close.iloc[i]
#             c = df_close[i:i+span]
#             a = list(map(lambda x: x-close, c))
#             b = list(map(lambda x, p: ((span-p)/span)*x, a, range(span)))

#             acc.append(uf.log_abs(max(b) + min(b),
#                        zeros=True)/uf.log_abs(close))
#         else:
#             acc.append(None)

#     return acc if not type(limit) == float or type(limit) == int else uf.classify(acc, limit)

def get_wr_target(df_close: list[float], span: int, limit, peak: False):
    """returns weighted range target given df['close']. Use limit=False to not
    classify, else float. Use peak=True to get places to sell"""
    acc = []
    df_len = len(df_close)

    for i in range(len(df_close)):

        if i+span < df_len:
            close = df_close.iloc[i]
            c = df_close[i:i+span]
            a = list(map(lambda x: x-close, c))
            b = list(map(lambda x, p: ((span-p)/span)*x, a, range(span)))

            acc.append(uf.log_abs(max(b) + min(b),
                       zeros=True)/uf.log_abs(close))
        else:
            acc.append(None)
    if peak:
        acc = list(map(lambda x: -x if x != None else None, acc))

    return acc if not type(limit) == float or type(limit) == int else uf.classify(acc, limit)


def zip_target(target: list[int], indicator: list[int]):
    """
    returns a new target of AND target and indicator. indicator must be list of
    int and of same length
    """
    return list(map(lambda t, i: t and i, target, indicator))
