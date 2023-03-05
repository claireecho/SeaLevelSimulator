from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
ad = open("Axyz.txt", "w")
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

sd.write(str(sortData)+ "\n")
sd2 = open("Sxyz.txt", "r").read().split()

while i < len(sortData):
    adData.append(((float(sortData[i][n]))+89)*150-1500)
    i+=1

        
ad.write(str(adData) + "\n")

    
