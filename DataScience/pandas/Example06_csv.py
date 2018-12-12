import pandas as pd 

dataFrame = pd.read_csv("scottish_hills.csv")

#print first 10
print(dataFrame.head(10))

#sort by height

sorted_hills = dataFrame.sort_values(by=['Height'],ascending=False)
print(sorted_hills.head(5))