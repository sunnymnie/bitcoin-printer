# Feature analysis template

Naming convention: `indicator type`-`indicator name`.csv

Use lowercase with `-`, use indicator name abbreviation as seen on README.md

## Intro to indicator
Purpose: mostly to get to know about the indicator and to import dependencies

### Header cell: 
- Name of indicator
- (correlations and feature analysis)

### About cell 
- Short summary and notes of indicator. Read through [documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html)
- About and calculation: Go over the technical terms of the indicator. Briefly go over how the indicator is calculated
- Usage: How to traders use this indicator? What do traders use the indicator to verify, filter, etc? 
- Notes: Some random facts that may or may not be pertaining to the indicator in question. 

### Imports cell
Read through documentation on how to import indicator in question.
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import useful_functions as uf
import classification_report_generator as crg
# from ta.trend import SMAIndicator # figure out to import indicator in question
```

### Read DataFrame cell
Import base dataframe. 
```python
df = pd.read_csv("../data/BTCUSDT-hour-target.csv")
```
## Check base indicator variations
Purpose: Check if default variations has the highest correlation or if there is some other variation with greater correlation. Check the default correlation with target. Is it high (ie, above 0.15), or low (ie, below 0.05). 
- If high, consider goldmine!
- If low, still do the other steps, but if it's continually low consider finishing segment. 

### Create variation making function
Create a function that can generate some variations of the data (ie chaning window length and other paramaters if possible)
```python
def variations(windows:list[int]):
    """
    returns variations of atr indicator with given windows
    """
    name = "atr_"
    for w in windows:
        atr = AverageTrueRange(df["high"], df["low"], df["close"], w)
        df[name + str(w)] = atr.average_true_range()
```
### Create log version of indicator
```python
df["atr_log"] = list(map(lambda x: uf.log_abs(x, zeros=True), df.atr_14))
```

### Plot correlation matrix
Check:
- correlation with target
- correlation amongst indicators

```python
indicators = list(df.columns)[13:]
indicators.append("target")

d = df[list(indicators)].copy()
corr_matrix = d.corr()
fig, ax = plt.subplots(figsize=(10, 7))
ax = sns.heatmap(corr_matrix,
                 annot=True,
                 linewidths=0.5,
                 fmt=".2f",
                 cmap="YlGnBu")

```

## Variations of indicator with highest correlation
If: 
- correlation with target is relatively the same amongst indicators (differing by no more than 0.05 from default paramater)
- correlation amongst indicators is high (greater than 0.8)

Pick either indicator variation with default paramaters. 

Else if correlation with target is relatively different (differing by more than 0.05 from default paramater): Pick indicator with default paramaters AND indicator with highest correlation

**Note**: Remember to always plot correlation matrix and graphs

### Plot indicator to get to know more about it
- Does it follow closing price somewhat? More work needed
- Does it seem to NOT fit within a range (ie, [0, 20])? More work needed. 

**If indicator follows closing price somewhat:** Calculate indicator divided by closing price

**If indicator doesn't seem to fit within a range:** Calculate log variation. Use np.log_abs(x, zeros=True) if taking log of 0. 


### Rate of change
- Get moving average, then find the rate of change. Take division over closing price and log if necessary. 

### Second derivative
- Take rate of change of previously calculated moving average. Take division over closing price and log if necessary. 

## Feature importance

Run all crg commands. (can find at crg-examples.ipynb)

## Make cell under header summarizing findings
Include precision, recall, and f1

Make table including what you think are the most important features. 
- For each group of features that have high correlations between eachother, pick one. 
- If features have a correlation less than 0.1 with the target, consider not adding. 
- Consider picking features with a higher feature-importance than the feature with the highest correlation
- Order table by correlation to target until it's features picked with highest feature-importance. Order those below features with high correlation in feature-importance order. 

| Metric | Selected paramaters | All paramaters |
| ---: | :---: | :---: |
| Precision | 0.211| 0.139|
| Recall |0.250 | 0.251|
| F1 |0.083 |0.079 |

| Name | Correlation | Importance |
| --- | :---: | :---: |
| atr_o_close | 0.21 | 0.085|
| atr_14 | 0.19 | 0.049|
| atr_200 | 0.18 | 0.124|
| atr_100 | 0.19 | 0.101|
| atr_50 | 0.19 | 0.084|
| atr_ma_2 | 0.19 | 0.096|



```markdown
| Metric | Selected paramaters | All paramaters |
| ---: | :---: | :---: |
| Precision | 0.211| 0.139|
| Recall |0.250 | 0.251|
| F1 |0.083 |0.079 |

| Name | Correlation | Importance |
| --- | :---: | :---: |
| atr_o_close | 0.21 | 0.085|
| atr_14 | 0.19 | 0.049|
| atr_200 | 0.18 | 0.124|
| atr_100 | 0.19 | 0.101|
| atr_50 | 0.19 | 0.084|
| atr_ma_2 | 0.19 | 0.096|

```

