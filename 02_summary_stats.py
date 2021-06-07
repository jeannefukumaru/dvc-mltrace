import pandas as pd 

a = pd.read_csv('abalone.csv')
print('counting null values')
print(a.isna().sum())
