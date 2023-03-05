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
canvas = Canvas(root,width=w,height=h,bg='blue')
def makeAlabamaGA():
   canvas.create_polygon(rat, f="yellow", outline="#023020", width=1)
   
while i < len(mensa):
   try: 
      if n==0:
         rat.append(((float(mensa[i]))+89)*150-1500)
         n=1
      else:
         rat.append(((float(mensa[i]))-30)*-150+1450)
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
   
def plotPoints():
   u=0
   while u < len(f):
     # if float(f[u+2]) < 0:
      canvas.create_rectangle(f[u], f[u+1], f[u], f[u+1], f="green")
      u+=3
plotPoints()


canvas.pack()
               
root.mainloop()
