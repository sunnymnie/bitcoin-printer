import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def frac_diff_ffd(series,d,thres=1e-5):
    '''
    Constant width window (new solution)
    Note 1: thres determines the cut-off weight for the window
    Note 2: d can be any positive fractional, not necessarily bounded [0,1].
    '''
    #1) Compute weights for the longest series
    w=get_weights_ffd(d,thres)
    width=len(w)-1
    #2) Apply weights to values
    df={}
    for name in series.columns:
        series_f =series[[name]].fillna(method='ffill').dropna()
        df_=pd.Series(dtype=float)
        for iloc1 in range(width,series_f.shape[0]):
            loc0,loc1=series_f.index[iloc1-width],series_f.index[iloc1]
            if not np.isfinite(series.loc[loc1,name]):continue # exclude NAs
            df_[loc1]=np.dot(w.T,series_f.loc[loc0:loc1])[0,0]
        df[name]=df_.copy(deep=True)
    df=pd.concat(df,axis=1)
    return df

def get_weights_ffd(d,thres):
    """thres>0 drops insignificant weights"""
    w,k=[1.],1
    while True:
        w_=-w[-1]/k*(d-k+1)
        if abs(w_)<thres:break
        w.append(w_)
        k+=1
    w=np.array(w[::-1]).reshape(-1,1)
    return w