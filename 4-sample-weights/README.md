# Sample Weights
## Section 1: Adding sample weights
Generate number of co-events, and then average uniqueness and weights. Generate time decay and create weighted time decay `wd`. 

Files needed: 
- BTCUSDT-volume-bars.csv
- t1.csv

Files created:
- weighted_t1.csv

## Section 2: Sequential bootstrap
Performs a sequential boostrap to generate a new t1 with greater average uniqueness to being sample closer to IID. Note: takes a long time. 

Files needed: 
- t1.csv

Files created:
- seq_bootstrap.csv `sb = pd.to_datetime(pd.read_csv("../data/seq_bootstrap.csv", index_col=0, parse_dates=True, squeeze=True))`

## Section 3: Weighted Boostrap: Merge weights and sequential bootstrap
Merging both files created in section 1 and section 2. 

Files needed: 
- weighted_t1.csv
- seq_bootstrap.csv

Files created:
- weighted_seq_bootstrap.csv `wsb = pd.read_csv("../data/weighted_seq_bootstrap.csv", index_col=0, parse_dates=[0, 5])`

