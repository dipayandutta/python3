import csv
import sys
import numpy as np

csv_file = open("/code/python3/DataScience/dataFiles/sonar-all-data.csv","r")

read = list(csv.reader(csv_file,delimiter=","))

rowCount = 0
colCount = 0
ColData = []
colData_float = []
for row in read:
	 rowCount += 1

for col in read:
	 colCount += 1

for line in read:
	 ColData.append(line[3])

for data in ColData:
	 colData_float.append(float(data))

#print (colData)

colArray = np.array(colData_float)
colMean  = np.mean(colArray)
colSD	   = np.std(colArray)

sys.stdout.write("Mean = "+'\t'+str(colMean)+'\t\t')
sys.stdout.write("Standard Deviation = "+'\t'+str(colSD))
sys.stdout.write("\n")

# Calculate the quantile boundaries
ntiles = 4
percentBdry = []

for i in range(ntiles+1):
	 percentBdry.append(np.percentile(colArray,i*(100)/ntiles))

sys.stdout.write("\t Boundaries for 4 Eqaul Percentiles \n")
print(percentBdry)
sys.stdout.write("\n")

# The last column contains categorical variables
colData_last =[]

for line in read:
	 ColData.append(line[60])
for data in ColData:
	 colData_last.append(float(data))

unique = set(colData_last)
print(unique)
