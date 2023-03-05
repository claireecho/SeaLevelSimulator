from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
sortData = []
adData = []
i=0

# Implement text into 2D array
while i< len(d):
    temp = []
    for j in range(3):
        temp.append(float(d[i]))
        i+=1
    sortData.append(temp)

# Sort the 2D array using index 2
for i in range(len(sortData)):
    for j in range(i, len(sortData)):
        if sortData[i][2] > sortData[j][2]:
            temp = sortData[i]
            sortData[i] = sortData[j]
            sortData[j] = temp

# Converting sorted data into appropriate coordinates
for i in range(len(sortData)):
    adData.append([(sortData[i][0]+89)*150-1500, (sortData[i][1]-30)*-150+1450, sortData[i][2]])


# Writing into separate files
sd.write(str(adData)+ "\n")
    
