from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
sortData = []
adData = []
i=0
while i< len(d)/1000:
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)
    

print(sortData)
n=0
while i < len(sortData):
    if n==0:
        adData.append(((float(sortData[i]))+89)*150-1500)
        n=1
    else:
        adData.append(((float(sortData[i]))-30)*-150+1450)
        n=0
sd.write(str((Sort(sortData)))+ "\n")


    
