from pandas import DataFrame,read_csv
import pandas as pd 

file = r'sample.csv'
df = pd.read_csv(file)

print(df)

# High Score 
print('High Score ',df['Highscore'].max())
print('Low Score',df['Highscore'].min())