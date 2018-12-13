import numpy as np
import pylab
import scipy.stats as stats
import sys
import csv

csv_file = open("/code/python3/DataScience/dataFiles/sonar-all-data.csv")
read = list(csv.reader(csv_file,delimiter=","))

rowCount = 0
colCount = 0
colData = []
colData_float = []

# Row numbers
for row in read:
	 rowCount +=1 

# Column Counts
for col in read[0]:
	 colCount += 1

for line in read:
	 colData.append(line[3])

for data in colData:
	 colData_float.append(float(data))

print (colData_float)
stats.probplot(colData_float,dist="norm",plot=pylab)
pylab.show()
