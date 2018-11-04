import time
import itertools
password = "P@ssw0rd#"
print ("Cracking...")
start = time.time()
for test in itertools.product('abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*1234567890', repeat = 9):
    print("".join(test))
    if "".join(test) == password:
        stop = time.time()
        print ("".join(test), "match found! Process took {0} seconds".format(stop - start))
        
        break
    else:
        continue
