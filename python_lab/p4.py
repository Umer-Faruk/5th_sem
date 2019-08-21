import pandas as pd
# #series
# my_series=pd.Series([1, 5, 6, 9])
# print(my_series)
# print(my_series.index)
# print(my_series.values)
# print(my_series[2])
# series2=pd.Series([1, 5, 6, 9, 4], index=['a', 'b', 'c', 'd', 'f'])
# print(series2)
# print(series2 > 5)
# series2.name='number'
# series2.index.name='leters'
# print(series2)

# #DataFrame
# df1=pd.DataFrame({
#     'numbers':[1, 2, 3, 4],
#     'names':['umer', 'ramesh', 'faruk', 'raj']
# },index=['u', 'r', 'f', 'R'])
# print(df1)
# #print(df1['numbers'])
# print(df1.index)
# print(df1.columns)
# print(df1.loc['u'])
# print(df1.iloc[0])
# print(df1.reset_index())
# df1.to_csv('detail.csv')
tita_df=pd.read_csv('titanic.csv')
print(tita_df.head())
print(tita_df.groupby(['Sex', 'Survived'])['PassengerID'].count())

