# Labelling
## Section 1: Volatility and Serial Correlation
Generate volatilites and serial correlation. Folder include notebooks to generate different types of volatilities besides default exponentiated moving average of log returns or whatever that was. 

Files needed: 
- BTCUSDT-volume-bars.csv

Files created:
- vol.csv
- serial-correlation.csv

## Section 2: Non-ML Strategy
Generate side.csv via a non-ML or simple ML strategy. Folder includes variety of different strategies. Make sure to swap notebooks to use different strategies. 

Files needed: 
- BTCUSDT-volume-bars.csv

Files created:
- side.csv (depreciated)
- metalabels.csv (with kalman strat)

## Section 3: Meta-labelling
Make the complete meta-labelling file, ending up with a dataframe with 'target' (to train ML model), 'side' (non-ML model's prediction), 'ret' (the return of non-ML model's bet), and 'sc' which is serial correlation. 

Files needed: 
- BTCUSDT-volume-bars.csv
- vol.csv
- serial-correlation.csv
- side.csv

Files created:
- metalabels.csv
- t1.csv `t1 = pd.to_datetime(pd.read_csv("../data/t1.csv", index_col=0, parse_dates=True, squeeze=True))`

Optional creations:
- events.csv `events = pd.read_csv("../data/events.csv", index_col=0, parse_dates=[0, 1])`