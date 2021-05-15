# Bitcoin Printer 

## Immediate tasks:
- create `classificationreportgenerator.py` in `analysis-features` that automatically does what `c-report-gen.ipynb` currently fulfills. 

## Month-end goal (May 31st):
A Scikit-learn model that predicts the price of Bitcoin given matches to technical indicators and other indicators like the stock-to-flow model

## Further goals:
A filter that can spot promising alt-coins or a model that can predict alt-coin price movements. 

## Plan:
1. Find out where to get my data and find the most efficient method
2. Learn about technical analysis and which indicators I think my next programs must/should/could include. 
3. Find if there exists any dependencies that automatically creates technical indicators from time-series-data. 
    - If yes: learn to use them
    - If yes or no: aim to make some technical indicators by hand (especially those that are more obscure, such as logarithmic-growth)
4. Create a price-analyzer program. Regard to information about this project below
5. Learn time series data prediction with Scikit-learn module on regression + start data exploratory phase
6. Create scikit-learn model based on dataset from price-analyzer program. 


### Price analyzer program
This program will end up forming the backbone of the inputs to the ml model, but can exist as a separate equally useful program. 

Program purpose: Given past price movements of currency X, gives a dictionary (or dataframe) containing values to all existing technical indicators. As an extension, can perform some brute-force simple arithmetic to give a semi-meaningful number result. 

Remake for ml model: return dataframe with columns for each indicator (Make sure this is consistent with what's taught)

## Plan results + notes + directory
### 1. Where to get my data:

Requirements:
- Free and reliable
- Is continually updated
- 

**[kaggle](https://www.kaggle.com/tencars/392-crypto-currency-pairs-at-minute-resolution?select=algusd.csv)**

Pros: `1 minute detail`

Cons: 

Unknowns: `reliability` `updated`

**binance**

Will probably go with Binance. If it works I'm probably not going to test others unless Binance breaks. 

[where to get past crypto data](https://fxgears.com/index.php?threads/how-to-acquire-free-historical-tick-and-bar-data-for-algo-trading-and-backtesting-in-2020-stocks-forex-and-crypto-currency.1229/#post-19305)

Ran code:
`pip3 install python-binance`



### 2. Technical analysis 

Using technical analysis [package](https://github.com/bukosabino/ta) `conda install -c conda-forge ta`

Plan: Given that 'all indicators' method is broken, I will have to add each one individually. The first few I will add will be ones that (1) Are covered in Coin Bureau's indicators list, (2) exists in the library. + I get to learn the data. 

[ta documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html)

[ta github](https://github.com/bukosabino/ta)

#### Sources to research:
- [Coin Bureau](https://www.youtube.com/watch?v=lW3eWIj3Q04)
- [the trading channel](https://www.youtube.com/watch?v=eynxyoKgpng)

DONE above researching

### 3. Add technical analysis to time-series-data

Done adding technical analysis data. Csvs with technical analysis are named "...-features.csv". 

### 4. Create price-analyzer side project

Skip. Current implementation presents all indicators without UI. Plus this project is flawed in the beginning as it assums I can find the best weights and balances to make meaning from technical analysis. 

### 5. Start and finish regression module + work on data exploratory side-projects

End goal: Finish and understand the regression module at the same time when all data exploratory side-projects are finished. 
Data exploratory side-projects include the correlation matrix, matplotlib feature and target comparision, etc. 

### 6. Create ML regression (or classification group)

[interesting reddit comment strategy](https://www.reddit.com/r/algotrading/comments/ipa112/what_target_do_your_algo_aim_to_predict_price/)



### Need to do:
- Need to create correlation matrix for all available indicators, pick the highest abs(correlation) and create variations and create ml algos to work on versions of those and analyze feature importance and pick highest (also forward test on Jan 2021 + data (don't train on those))

### Technical indicators
- https://www.youtube.com/watch?v=9_Bs5R66NxY
- bull flag. up then slight pullback with decrease in selling volume. if selling is high = price correction. 
    - pole starts as dip in uptrend
    - usual gain: bottom of pole to top of pole distance
- falling wedge: gain price = largest movement in price of wedge on leftest side
- W and M patterns, w is bullish
- fib retracement
- btc dominance
- 