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
mid40 = open("mid40.txt", "w")
mid60 = open("mid60.txt", "w")
mid80 = open("mid80.txt", "w")
mid100 = open("mid100.txt", "w")
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
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.25])
    file40 += str(m40[i][0]) + " " + str(m40[i][1]) + " " + str(m40[i][2]) + "\n"
    m60.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.45])
    file60 += str(m60[i][0]) + " " + str(m60[i][1]) + " " + str(m60[i][2]) + "\n"
    m80.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-0.71])
    file80 += str(m80[i][0]) + " " + str(m80[i][1]) + " " + str(m80[i][2]) + "\n"
    m100.append([(sortData[i][0]+89)*150-1500,
                   (sortData[i][1]-30)*-150+1440, sortData[i][2]-1.0])
    file100 += str(m100[i][0]) + " " + str(m100[i][1]) + " " + str(m100[i][2]) + "\n"


        
mid40.write(file40)
mid60.write(file40)
mid80.write(file40)
mid100.write(file40)


    
