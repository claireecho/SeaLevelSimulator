from tkinter import *
from PIL import Image, ImageTk

global canvas
w,h=640,480
jerome = open("vaANDmd.txt", "r").read()
i = 0
n=0
mensa = jerome.split()
rat = []
f = open("Axyz.txt", "r").read().split()
root=Tk()
canvas = Canvas(root,width=w,height=h,bg='palegreen4')
def plotPoints():

   u=0
   while u < len(f):
      if float(f[u+2]) < 0:
         if float(f[u])>169.43700000000058:
            canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                    float(f[u+1])+7, fill="blue",
                                    outline="blue")
      elif float(f[u+2])<13:
         canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                 float(f[u+1])+7, fill="#365936",
                                 outline="#365936")
      elif float(f[u+2])<25:
         canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                 float(f[u+1])+7, fill="#457345",
                                 outline="#457345")
      elif float(f[u+2])<50:
         canvas.create_rectangle(float(f[u]), float(f[u+1]), float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen4",
                                 outline="palegreen4")
      elif float(f[u+2])<100:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen3",
                                 outline="palegreen3")
      elif float(f[u+2])<200:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen2",
                                 outline="palegreen2")
         
      elif float(f[u+2])<300:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen1",
                                 outline="palegreen1")
      elif float(f[u+2])<400:
         canvas.create_rectangle(float(f[u]), float(f[u+1]),
                                 float(f[u])+7,
                                 float(f[u+1])+7, fill="palegreen",
                                 outline="palegreen")
      elif float(f[u+2])<600:
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
