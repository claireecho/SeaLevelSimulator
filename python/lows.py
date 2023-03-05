from array import *
h = open("xyz.txt", "r").read()
d= h.split()
sd = open("Sxyz.txt", "w")
ad = open("Axyz.txt", "w")
sortData = []
adData = []
m40= []
m60= []
m80= []
m100= []
low40 = open("low40.txt", "w")
low60 = open("low60.txt", "w")
low80 = open("low80.txt", "w")
low100 = open("low100.txt", "w")
file40 = ''
file60 = ''
file80 = ''
file100 = ''


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

for i in range(len(sortData)):
    m40.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.18])
    file40 += str(m40[i][0]) + " " + str(m40[i][1]) + " " + str(m40[i][2]) + "\n"
    m60.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.29])
    file60 += str(m60[i][0]) + " " + str(m60[i][1]) + " " + str(m60[i][2]) + "\n"
    m80.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.4])
    file80 += str(m80[i][0]) + " " + str(m80[i][1]) + " " + str(m80[i][2]) + "\n"
    m100.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.5])
    file100 += str(m100[i][0]) + " " + str(m100[i][1]) + " " + str(m100[i][2]) + "\n"


        
low40.write(file40)
low60.write(file40)
low80.write(file40)
low100.write(file40)


    
