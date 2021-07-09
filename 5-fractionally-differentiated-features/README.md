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

## Scoring paramaters:
| Score | Description |
| :---: | :--- |
| ⭐ | Top 10% of indicators scored on MDI including random, `side`, `sc` |
| ✔️ | Top 30% |
| ❗️ | Bottom 30% |
| 🛑 | Bottom 10% |
| ❌ | Worst indicator |


## Files created:

| Name | Score | Procedure |
| :---: | :---: | --- |
| `i0` | ✔️ | `AwesomeOscillatorIndicator(df.high, df.low, 500, 3400)` |
| `i1` |  | `AwesomeOscillatorIndicator(df.high, df.low, 5000, 34000)` |
| `i2` |  | `KAMAIndicator(df.close, 10000, 2, 30)` then `indicator = df.close - indicator` |
| `i3` |  | `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo()` |
| `i4` |  | `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo_hist()` |
| `i5` |  | `PercentagePriceOscillator(df.close, 2600, 1200, 900)` `i.ppo_signal()`|
| `i6` | ✔️ | `ROCIndicator(df.close, 1200)`|
| `i7` |  | `ROCIndicator(df.close, 12000)`|
| `i8` | ✔️ | `RSIIndicator(df.close, 1000)`|
| `i9` | ⭐ | `RSIIndicator(df.close, 10000)`|
| `i10` | ❌ | `StochRSIIndicator(df.close, 7000, 150, 150)` `stochrsi()`|
| `i11` |  | `StochRSIIndicator(df.close, 7000, 150, 150)` `stochrsi_d()`|
| `i12` |  | `StochRSIIndicator(df.close, 14000, 300, 300)` `stochrsi_k()`|
| `i13` | 🛑 | `StochasticOscillator(df.high, df.low, df.close, 14000, 300)` `stoch()`|
| `i14` |  | `StochasticOscillator(df.high, df.low, df.close, 10000, 200)` `stoch_signal()`|
| `i15` |  | `TSIIndicator(df.close, 2500, 1300)`|
| `i16` | ✔️ | `df.iloc[::200, :].close` with `d-val = 0.45` and `thres = 1e-5`|
| `i17` | ❗️ | `BollingerBands(df.close, 2000, 2)` `bollinger_pband()` |
| `i18` | ✔️ | `BollingerBands(df.close, 20000, 2)` `bollinger_pband()` |
| `i19` | ❗️ | `BollingerBands(df.close, 2000, 2)` `bollinger_wband()` |
| `i20` | ⭐ | `BollingerBands(df.close, 20000, 2)` `bollinger_wband()` |
| `i21` | 🛑 | `DonchianChannel(df.high, df.low, df.close, 2000)` `donchian_channel_pband()` |
| `i22` | ❗️ | `DonchianChannel(df.high, df.low, df.close, 20000)` `donchian_channel_pband()` |
| `i23` | ❗️ | `DonchianChannel(df.high, df.low, df.close, 2000)` `donchian_channel_wband()` |
| `i24` | ✔️ | `DonchianChannel(df.high, df.low, df.close, 20000)` `donchian_channel_wband()` |
| `i25` | ❗️ | `KeltnerChannel(df.high, df.low, df.close, 2000, 1000)` `keltner_channel_pband()` |
| `i26` |  | `KeltnerChannel(df.high, df.low, df.close, 20000, 10000)` `keltner_channel_pband()` |
| `i27` |  | `KeltnerChannel(df.high, df.low, df.close, 2000, 1000)` `keltner_channel_wband()` |
| `i28` | ⭐ | `KeltnerChannel(df.high, df.low, df.close, 20000, 10000)` `keltner_channel_wband()` |
| `i29` |  | `UlcerIndex(df.close, 1400)` |
| `i30` | ❗️ | `UlcerIndex(df.close, 14000)` |
| `i31` | 0 |  |
| `i32` | 0 |  |
| `i33` | 0 |  |
| `i34` | 0 |  |
| `i35` | 0 |  |
| `i36` | 0 |  |
| `i37` | 0 |  |
| `i38` | 0 |  |