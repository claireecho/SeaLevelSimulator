from tkinter import *
from PIL import Image, ImageTk

global canvas
w,h=640,480
jerome = open("vaANDmd.txt", "r").read()
i = 0
n=0
mensa = jerome.split()
rat = []
f = open("min100.txt", "r").read().split()
root=Tk()
canvas = Canvas(root,width=w,height=h,bg='blue')
def plotPoints():
   u=0
   while u < len(f):
      if float(f[u+2]) < 0:
         canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                 float(f[u+1])+7, fill="blue",
                                 outline="blue")
      elif float(f[u+2])<49:
         canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen4",
                                 outline="palegreen4")
      elif float(f[u+2])<99:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen3",
                                 outline="palegreen3")
      elif float(f[u+2])<199:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen2",
                                 outline="palegreen2")
         
      elif float(f[u+2])<299:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen1",
                                 outline="palegreen1")
      elif float(f[u+2])<399:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen",
                                 outline="palegreen")
      elif float(f[u+2])<700:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegoldenrod",
                                 outline="palegoldenrod")
      u+=3
plotPoints()

def makeAlabamaGA():
   canvas.create_polygon(rat, fill= '', outline="black", width=1)
   
while i < len(mensa):
   try: 
      if n==0:
         rat.append(((float(mensa[i]))+89)*150-1500)
         n=1
      else:
         rat.append(((float(mensa[i]))-30)*-150+1440)
         n=0
   except ValueError:
      if mensa[i]=='END_ONE_POLY':
         makeAlabamaGA()
         rat.clear()
      if mensa[i]== 'END_ALL_POLY':
         rat.clear()
      if mensa[i]== 'END_FILE':
         break
   i+=1
   


canvas.pack()
               
root.mainloop()
