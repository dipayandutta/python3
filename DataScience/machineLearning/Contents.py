import csv
import sys

csv_file = open("/code/python3/DataScience/dataFiles/sonar-all-data.csv","r")

read = list(csv.reader(csv_file,delimiter=","))

rowCount = 0
colCount = 0

# Total number of rows
for row in read:
	 rowCount+=1

# Total number of columns
for col in read[0]:
	 colCount += 1

print (rowCount)
print (colCount)

type = [0]*3
colCounts = []

for col in range(colCount):
	 for row in read:
			try:
				 a = float(row[col])
				 if isinstance(a,float):
						type[0] += 1
			except ValueError:
				 if len(row[col]) > 0:
						type[1] += 1
				 else:
						type[2] += 1

	 colCounts.append(type)
	 type = [0]*3


sys.stdout.write("Col#"+'\t'+"Numbers"+'\t'+"String"+'\t'+"Others\n")

iCol =0
for types in colCounts:
	 sys.stdout.write(str(iCol)+'\t\t'+str(type[0])+'\t\t'+str(types[1])+'\t\t'+str(type[2])+"\n")


