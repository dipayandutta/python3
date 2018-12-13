import collections

dict1 = {'source':'kolkata','destination':'Baruipur'}
dict2 = {'breakfast':'bread & butter' , 'launch':'Briyani'}

print ("First Dict")
print (dict1)
print ("Second Dict")
print (dict2)

# Makeing a single dict from both dict
dict1_dict2 = collections.ChainMap(dict1,dict2)
print(dict1_dict2)
print("==========================================")
print(dict1_dict2.maps)

#print keys of the dictonary
print('Keys = {} '.format(list(dict1_dict2.keys())))
#print values of the dictonary
print('values = {}'.format(list(dict1_dict2.values())))

# print all the elements in the dict
for key,value in dict1_dict2.items():
    print(key+" ==> "+value)

