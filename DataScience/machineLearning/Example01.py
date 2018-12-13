import csv

csv_file = open("/code/python3/DataScience/dataFiles/sonar-all-data.csv","r")

read = list(csv.reader(csv_file,delimiter=","))

rowCount = 0
colCount = 0

# Number of rows
for row in read:
	 rowCount += 1

#Number of Columns
for col in read[0]:
	 colCount += 1

print("Total number of columns "+str(colCount))
print ("Total number of rows "+str(rowCount))
