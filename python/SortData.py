from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
sortData = []
adData = []
i=0
#d.remove(",")
while i< len(d):
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)
#print(sortData)

for i in range(len(sortData)):
    for j in range(i, len(sortData)):
        if sortData[i][2] > sortData[j][2]:
            temp = sortData[i]
            sortData[i] = sortData[j]
            sortData[j] = temp

n=0
while i < len(sortData):
    if n==0:
        adData.append(((float(sortData[i]))+89)*150-1500)
        n=1
    else:
        adData.append(((float(sortData[i]))-30)*-150+1450)
        n=0
sd.write(str(sortData)+ "\n")
    
