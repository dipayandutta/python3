#DataFrame creation Example

import pandas as pd 

scientist = pd.DataFrame({
	'Name':['Rosaline Franklin','William Gosset'],
	'Occupation':['Chemist','Statistician'],
	'Born':['xx-xx-xxxx','yy-yy-yyyy'],
	'Age':['30','40']
	},index=['First','Second'],
	columns=['Name','Occupation','Born','Age'])


print (scientist)

ages = scientist['Age']
print(ages)

#Mean of Ages of the scientists 
print(ages.mean())
#Min age 
print(ages.min())
#Maximum Age
print(ages.max())
