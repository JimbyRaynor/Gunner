import math
import sys
import os
import time
from tkinter import * 

sys.path.insert(0, os.path.expanduser("~/Documents"))
import LEDlib

# for loading files (.png, .txt), set current directory = location of this python script (needed for Linux)
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

def ColourTextSquare(x,y,mytext,charwidth,size):
    LEDlib.LEDtextobj(canvas1,x=x,y=y,text=mytext,colour="light green",pixelsize = size, charwidth=charwidth, solid = False, square=True)

def ColourText(x,y,mytext,charwidth,size):
    LEDlib.LEDtextobj(canvas1,x=x,y=y,text=mytext,colour="light green",pixelsize = size, charwidth=charwidth, solid = False, square=False)

def smalltext(x,y,mytext):
    ColourText(x,y,mytext,8*2-2,2)

MAXx = 1914
MAXy = 900

mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

canvas1.create_rectangle(2,2,MAXx-2,MAXy-2,outline="yellow")

titletext = ColourTextSquare(x=20,y=20,mytext="Gunner",charwidth=8*12-10,size=12)

instext1 = smalltext(1000,20,"You are the officer-in-charge giving orders to a gun crew,")
instext2 = smalltext(1000,40,"telling them the degrees of elevation you estimate")
instext3 = smalltext(1000,60,"will place a projectile on target.")
instext4 = smalltext(1000,80,"A hit within 100 metres of the target will destroy it.");


mainwin.mainloop()