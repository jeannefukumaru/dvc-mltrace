import pandas as pd 

a = pd.read_csv('data/abalone.csv')
print('counting null values')
print(a.isna().sum())
print('counting number of rows')
print(a.shape[0])
print('counting number of columns')
print(a.shape[1])
