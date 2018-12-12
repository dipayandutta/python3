import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.stats import linregress

dataFrame = pd.read_csv("scottish_hills.csv")

x = dataFrame.Height 
y = dataFrame.Latitude

stats = linregress(x,y)

m = stats.slope
b = stats.intercept 

#change the default figure size
plt.figure(figsize=(10,10))

#change the default marker fir the scatter from circle to x
plt.scatter(x,y,marker='x')

# Set the linewidth on the regression line to 3px
plt.plot(x,m*x+b,color="red",linewidth=3)

# Add x and y labels , and set their font size
plt.xlabel("Height (m)",fontsize=20)
plt.ylabel("Latitude ",fontsize=20)

# set the font size
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# show the plot
plt.show()