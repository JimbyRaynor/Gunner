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
    return LEDlib.LEDtextobj(canvas1,x=x,y=y,text=mytext,colour="light green",pixelsize = size, charwidth=charwidth, solid = False, square=True)

def ColourText(x,y,mytext,charwidth,size):
    return LEDlib.LEDtextobj(canvas1,x=x,y=y,text=mytext,colour="light green",pixelsize = size, charwidth=charwidth, solid = False, square=False)

def smalltext(x,y,mytext):
    return ColourText(x,y,mytext,8*2-2,2)

def medtext(x,y,mytext):
    return ColourText(x,y,mytext,8*3,3)

MAXx = 1914
MAXy = 900

mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

RetroScreen = LEDlib.scrollboxobj(canvas1,x=10,y=140,width=800,height=600)
instructionbox = LEDlib.scrollboxsmallobj(canvas1,x=1000,y=20,width=800,height=600)

canvas1.create_rectangle(2,2,MAXx-2,MAXy-2,outline="yellow")

titletext = ColourTextSquare(x=20,y=20,mytext="Gunner",charwidth=8*12-10,size=12)


instructionbox.scrollboxadd("Instructions")
instructionbox.scrollboxadd(" ")
instructionbox.scrollboxadd("You are the officer-in-charge giving orders to a gun crew,")
instructionbox.scrollboxadd("telling them the degrees of elevation you estimate")
instructionbox.scrollboxadd("will place a projectile on target.")
instructionbox.scrollboxadd("A hit within 100 metres of the target will destroy it.")
instructionbox.scrollboxadd(" ")
instructionbox.scrollboxadd(" ")
instructionbox.scrollboxadd(" ")


def on_close():
     global RetroScreen, instructionbox, titletext
     del RetroScreen
     del instructionbox
     del titletext
     mainwin.destroy()

def mykey(event):
    key = event.keysym
    if key in "0123456789":
        RetroScreen.scrollboxadd(key)
        

mainwin.protocol("WM_DELETE_WINDOW", on_close)
mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()