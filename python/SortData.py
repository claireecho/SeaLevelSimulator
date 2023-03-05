from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
sortData = []
file=''
i=0
#d.remove(",")

# Adding text to a 2D array
while i< len(d):
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)

# Sorting Method
for i in range(len(sortData)):
    for j in range(i, len(sortData)):
        if sortData[i][2] > sortData[j][2]:
            temp = sortData[i]
            sortData[i] = sortData[j]
            sortData[j] = temp


sd.write(str(sortData)+ "\n")
    
