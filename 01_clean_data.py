import pandas as pd 

raw = pd.read_csv('data/abalone.data', header=None)

print('adding column names')

raw.columns = ['sex','length','diameter','height','whole_weight','shucked_weight','viscera_weight','shell_weight','rings']

print('saving data to csv')

raw.to_csv('data/abalone.csv')

