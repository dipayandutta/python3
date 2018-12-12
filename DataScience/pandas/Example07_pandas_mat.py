import pandas as pd 
import matplotlib.pyplot as plt 

dataFrame = pd.read_csv('scottish_hills.csv')

x = dataFrame.Height
y = dataFrame.Latitude 

print (x)
plt.scatter(x,y)
plt.show()