# Bitcoin Printer 

## Immediate tasks:
- create `target.py` that hosts functions that are helpful for finding new targets
    - `get_wm_target()` that returns the weighted mean target with paramater for length and % gain
    - `normalize()` that takes in a list or pandas series and normalizes it to only have 0 and 1
    - `get_mapped_target()` that returns the `and` of each element from two lists
- find a more elegant solution to access python documents from other folders
- Update `classification_report_generator` to be more powerful that can return precision+f1+forwardtesting given only df. Perhaps call it `generate_report` and rename function already using that name

## Notes
- Tune the result of `get_mapped_target` to produce targets with between 10% and 15% ones. 
    - call Series.value_counts() to get number of 0s and 1s. 
    - Tune the wm_target's length and gain requirements

## Project goal: 
Create a Scikit-learn model that can reliably predict bitcoin dips

Also, emoji meanings: 
- ✅ Finished satisfactorily 
- 🟡 Finished, but might want to double check and perhaps re-do
- 🔴 Finished haphazardly, needs major make-over. (ie, for brainstorming sessions)
- ⬜ Todo
- ⭐ Currently working on/redoing

## Project timeline:
1. ✅ Download past Bitcoin data
2. ✅ Create basic technical indicators
3. ✅ Create basic target column and explore all available technical indicators
4. ⭐ Create variations of target and training models on each of the targets
    - Targets are made by mapping an indicator and keeping it as long as it makes money in the near future
    - Targets must cover the three cases: dips, flatline before jump in price, and buying during an uptrend
5. ⭐ Finding best hyperparamaters of each model and weeding out features with low feature importance. 
6. ⬜ Testing best representation of data for model. 
    1. Many classification models or just one? 
    2. Create concrete decision which features to keep and which to remove. 
7. ⬜ Create new model(s) for predicting local bitcoin peaks. 
    1. Re-create target column and basic technical indicators
    2. Use test with a variety of features, and include all selected features used for bitcoin dip model. 
    3. Re-consider how many models to use
8. ⬜ Create program that takes in bitcoin prices hourly and runs them by the models. Create UI and host model to run 24/7 with api-access to buy and sell on Binance. 
9. ⬜ Foward testing with small amounts of money. If unsuccessful consider if problem stems from model or from model-wrapper. Else, turn on bitcoin printer. 
10. ⬜ Expansion: predict stocks, altcoins, commodities, etc. 

**Sidequests (Optional, consider doing when reaching chokepoint)**
- Look into incorporating fundamental data / indicators
- Try to incorporate traditional technical patterns (triangle, support and resistance)
- Use TensorFlow (recommended after 9)

## Todolist `Optimizing and exploring paramaters / features`: 
**✅ Volume**
- ✅ Money Flow Index (MFI)
- 🟡 Accumulation/Distribution Index (ADI)
- 🟡 On-Balance Volume (OBV)
- ✅ Chaikin Money Flow (CMF)
- ✅ Force Index (FI)
- ✅ Ease of Movement (EoM, EMV)
- 🟡 Volume-price Trend (VPT)
- ✅ Negative Volume Index (NVI)
- 🟡 Volume Weighted Average Price (VWAP)

**✅ Volatility**
- ✅ Average True Range (ATR)
- ✅ Bollinger Bands (BB)
- ✅ Keltner Channel (KC)
- ✅ Donchian Channel (DC)
- ✅ Ulcer Index (UI)

**✅ Trend**
- ✅ Simple Moving Average (SMA)
- 🔴 Exponential Moving Average (EMA) ASSUMED same
- 🔴 Weighted Moving Average (WMA) ASSUMED same
- 🟡 Moving Average Convergence Divergence (MACD)
- ✅ AroonIndicator (ARN)
- ✅ Average Directional Movement Index (ADX)
- 🟡 Vortex Indicator (VI)
- 🟡 Trix (TRIX)
- 🟡 Mass Index (MI)
- ✅ Commodity Channel Index (CCI)
- ✅ Detrended Price Oscillator (DPO)
- 🔴 KST Oscillator (KST) Problem: 7 input variables, need to optimize
- ✅ Ichimoku Kinkō Hyō (ICH)
- 🟡 Parabolic Stop And Reverse (Parabolic SAR)
- 🟡 Schaff Trend Cycle (STC)

**✅ Momentum**
- ✅ Relative Strength Index (RSI)
- ✅ Stochastic RSI (SRSI)
- ✅ True strength index (TSI)
- 🔴🔴🔴 Ultimate Oscillator (UO) THERE"S 1000 INPUTS!!1 why? rip. 
- ✅ Stochastic Oscillator (SR)
- ✅ Williams %R (WR)
- ✅ Awesome Oscillator (AO)
- ✅ Kaufman's Adaptive Moving Average (KAMA)
- ✅🔴🟡 Rate of Change (ROC) ⭐⭐ JUST ROC CURVES? FROM 5 to 200?
- ✅ Percentage Price Oscillator (PPO)
- ✅ Percentage Volume Oscillator (PVO)

**⬜ Others**
- ⬜ Daily Return (DR)
- ⬜ Daily Log Return (DLR)
- ⬜ Cumulative Return (CR)

### Miscellaneous notes (remove if becomes useless)
- Indicator inspiration
    - bull flag. up then slight pullback with decrease in selling volume. if selling is high = price correction. 
        - pole starts as dip in uptrend
        - usual gain: bottom of pole to top of pole distance
    - falling wedge: gain price = largest movement in price of wedge on leftest side
    - W and M patterns, w is bullish
    - fib retracement
    - btc dominance

### Resources 
- [where to get past crypto data](https://fxgears.com/index.php?threads/how-to-acquire-free-historical-tick-and-bar-data-for-algo-trading-and-backtesting-in-2020-stocks-forex-and-crypto-currency.1229/#post-19305) `pip3 install python-binance`
- [technical analysis package](https://github.com/bukosabino/ta) `conda install -c conda-forge ta`
    - [ta documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html)
    - [ta github](https://github.com/bukosabino/ta)
- [Coin Bureau](https://www.youtube.com/watch?v=lW3eWIj3Q04)
- [the trading channel](https://www.youtube.com/watch?v=eynxyoKgpng)
- [interesting reddit comment strategy](https://www.reddit.com/r/algotrading/comments/ipa112/what_target_do_your_algo_aim_to_predict_price/)
- [technical indicator patterns](https://www.youtube.com/watch?v=9_Bs5R66NxY)