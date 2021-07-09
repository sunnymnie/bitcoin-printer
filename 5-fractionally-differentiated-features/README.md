# Sample Weights
## Section 1: (Optional) Analysis on stationarity
Determine for what minimum `d ∈ [0, 1]` the new series is stationary.

Files needed: 
- BTCUSDT-volume-bars.csv or `indicator/feature csv`

Results created:
- `d` value for ADF p-value < 0.05

## Section 2: Feature Differentiating
Differentiate the entire feature with 

Files needed: 
- BTCUSDT-volume-bars.csv or `indicator/feature csv`

Files created:
- `feature name`.csv



## Files created:
- `"../data/i0.csv"` is `AwesomeOscillatorIndicator(df.high, df.low, 500, 3400)`
- `"../data/i1.csv"` is `AwesomeOscillatorIndicator(df.high, df.low, 5000, 34000)`
- `"../data/i2.csv"` is `KAMAIndicator(df.close, 10000, 2, 30)` then `indicator = df.close - indicator`
- `"../data/i3.csv"` is `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo()`
- `"../data/i4.csv"` is `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo_hist()`
- `"../data/i5.csv"` is `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo_signal()`
- `"../data/i6.csv"` is `ROCIndicator(df.close, 1200)`
- `"../data/i7.csv"` is `ROCIndicator(df.close, 12000)`
- `"../data/i8.csv"` is `RSIIndicator(df.close, 1000)`
- `"../data/i9.csv"` is `RSIIndicator(df.close, 10000)`
- `"../data/i10.csv"` is `StochRSIIndicator(df.close, 7000, 150, 150)` `stochrsi()`
- `"../data/i11.csv"` is `StochRSIIndicator(df.close, 7000, 150, 150)` `stochrsi_d()`
- `"../data/i12.csv"` is `StochRSIIndicator(df.close, 14000, 300, 300)` `stochrsi_k()`
- `"../data/i13.csv"` is `StochasticOscillator(df.high, df.low, df.close, 14000, 300)` `stoch()`
- `"../data/i14.csv"` is `StochasticOscillator(df.high, df.low, df.close, 10000, 200)` `stoch_signal()`
- `"../data/i15.csv"` is `TSIIndicator(df.close, 2500, 1300)`
- `"../data/i16.csv"` is `df.iloc[::200, :].close` with `d-val = 0.45` and `thres = 1e-5`
- `"../data/i17.csv"` is 
- `"../data/i18.csv"` is 
- `"../data/i19.csv"` is 
