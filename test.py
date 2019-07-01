 
import hashlib 

with open('Data.txt') as f:
    lines = f.readlines()

for x in lines:
    y = x.split(',')
    for i in range(0, 10000):
        i = str(i).zfill(4)
        result = hashlib.md5(i.encode()) 
        #print(y[0])  
        
        if str(y[1]) == str(result.hexdigest()):
            print(result.hexdigest())

    