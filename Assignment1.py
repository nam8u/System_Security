 
import hashlib 

with open('Data.txt') as f:
    lines = f.readlines()

for x in lines:
    y = x.split(',')
    for i in range(0, 10000):
        i = str(i).zfill(4)
        result = hashlib.md5(i.encode()) 
         
        if str(i) == '1234':
            print(y[1])
            print(result.hexdigest())

    