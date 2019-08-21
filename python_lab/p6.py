import pandas as pd

weath = pd.read_csv('weather.csv')
print(weath.head())
print(weath.columns)
print(weath.index)
weath.columns =['old data', 'new data', 'old', 'new', 'daum']
# print(weath)
print(weath.groupby(['old data', 'old'])['new'])