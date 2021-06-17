# Bitcoin Printer 
Goal: Follow Advances in Financial Machine Learning and tweak

emoji meanings: 
- ✅ Finished satisfactorily 
- 🟡 Finished, but might want to double check and perhaps re-do
- 🔴 Finished haphazardly, needs major make-over. (ie, for brainstorming sessions)
- ⬜ Todo
- ⭐ Currently working on/redoing

## Project timeline:
1. ⬜ Form dollar bars for BTC and consider BTC futures:
    1. ⬜ Apply a symmetric CUSUM filter (Chapter 2, Section 2.5.2.1) where the threshold is the standard deviation of daily returns (Snippet 3.1).
    2. ⬜ Use Snippet 3.4 on a pandas series t1, where numDays = 1.
    3. ⬜ On those sampled features, apply the triple-barrier method, where ptSl = [1,1] and t1 is the series you created in point 1.b.
    4. ⬜ Apply getBins to generate the labels.
2. ⬜ From exercise 1, use Snippet 3.8 to drop rare labels.
3. ⬜ Adjust the getBins function (Snippet 3.5) to return a 0 whenever the vertical barrier is the one touched first.
4. ⬜ Develop a trend-following strategy based on a popular technical analysis statistic (e.g., crossing moving averages). For each observation, the model suggests a side, but not a size of the bet.
    1. ⬜ Derive meta-labels for ptSl = [1,2] and t1 where numDays = 1. Use as trgt the daily standard deviation as computed by Snippet 3.1.
    2. ⬜ Train a random forest to decide whether to trade or not. Note: The decision is whether to trade or not, {0,1}, since the underlying model (the crossing moving average) has decided the side, {−1,1}.
5. ⬜ Develop a mean-reverting strategy based on Bollinger bands. For each observation, the model suggests a side, but not a size of the bet.
    1. ⬜ Derive meta-labels for ptSl = [0,2] and t1 where numDays = 1. Use as trgt the daily standard deviation as computed by Snippet 3.1.
    2. ⬜ Train a random forest to decide whether to trade or not. Use as features: volatility, serial correlation, and the crossing moving averages from exercise 2.
    3. ⬜ What is the accuracy of predictions from the primary model (i.e., if the secondary model does not filter the bets)? What are the precision, recall, and F1-scores?
    4. ⬜ What is the accuracy of predictions from the secondary model? What are the precision, recall, and F1-scores?


### Resources 
- [where to get past crypto data](https://fxgears.com/index.php?threads/how-to-acquire-free-historical-tick-and-bar-data-for-algo-trading-and-backtesting-in-2020-stocks-forex-and-crypto-currency.1229/#post-19305) `pip3 install python-binance`
- [technical analysis package](https://github.com/bukosabino/ta) `conda install -c conda-forge ta`
    - [ta documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html)
    - [ta github](https://github.com/bukosabino/ta)
- [interesting reddit comment strategy](https://www.reddit.com/r/algotrading/comments/ipa112/what_target_do_your_algo_aim_to_predict_price/)
- [technical indicator patterns](https://www.youtube.com/watch?v=9_Bs5R66NxY)