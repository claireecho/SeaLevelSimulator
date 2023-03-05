from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
ad = open("Axyz.txt", "w")
sortData = []
adData = []

file = ''

i=0
while i< len(d):
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)

for i in range(len(sortData)):
    for j in range(i, len(sortData)):
        if sortData[i][2] > sortData[j][2]:
            temp = sortData[i]
            sortData[i] = sortData[j]
            sortData[j] = temp

sd.write(str(sortData)+ "\n")
sd2 = open("Sxyz.txt", "r").read().split()

for i in range(len(sortData)):
    adData.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1450, sortData[i][2]])
    file += str(adData[i][0]) + " " + str(adData[i][1]) + " " + str(adData[i][2]) + "\n"

        
ad.write(file)


    
