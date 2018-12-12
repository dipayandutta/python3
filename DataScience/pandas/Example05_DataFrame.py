import pandas as pd 

scottish_hills = {
	
	'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  
}

dataFrame = pd.DataFrame(scottish_hills)
print(dataFrame)
print(dataFrame.head(2))


print(dataFrame['Ben Macdui'])
print("location print")
print(dataFrame.iloc[0])