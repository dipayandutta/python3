import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import linregress 

dataFrame = pd.read_csv("scottish_hills.csv")

x = dataFrame.Height
y = dataFrame.Latitude

stats = linregress(x,y) #calculate the linear regression

m = stats.slope #get the slope
b = stats.intercept #get the intercept 

plt.scatter(x,y)
plt.plot(x,m*x+b,color="red")

plt.show()
