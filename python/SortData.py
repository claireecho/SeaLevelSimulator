from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
sortData = []
i=0
while i< len(d)/1000:
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)
def sortby(sortData):
    sortData.sort(key = lambda x: x[2])
    return sortData
print(sortData)


sd.write(str(sortData)+ "\n")
    
