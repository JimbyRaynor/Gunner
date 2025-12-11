import math
import sys
import os
import time
import random
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

RetroScreen = LEDlib.scrollboxobj(canvas1,x=10,y=140,width=1000,height=600)
instructionbox = LEDlib.scrollboxsmallobj(canvas1,x=1100,y=20,width=800,height=600)

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

r = random.randrange(20000,60000) # max range of gun
RetroScreen.scrollboxadd("Maximum range of your gun is "+str(r)+" metres")
RetroScreen.scrollboxadd(" ")

z = 0
s1 = 0
playeralive = True;

t = int(r*(.1+0.8*random.random())) # distance to target
RetroScreen.scrollboxadd("Distance to target is "+str(t)+" metres")


angle = 45
retroInputx = 1400
retroInputy = 400

def onclickPlus():
    global angle
    angle = angle + 1
    if angle > 89: angle = 89
    retroangletext.update(angle)

def onclickMinus():
    global angle
    angle = angle - 1
    if angle < 1: angle = 1
    retroangletext.update(angle)

s = 0
z = 0
def onclickFire():
    global s, z
    s = s + 1
    b = angle
    b2 = 2 * b / 57.3; # convert b to radians
    i0 = r * math.sin(b2)
    e = int(t - i0);
    if (abs(e) < 100):
       RetroScreen.scrollboxadd("*** Target destroyed *** "+str(s)+ " rounds of ammunition expended")
       enemyhit = True;
       z = z + 1
       if (z < 4):
         RetroScreen.scrollboxadd("The forward observer has sighted more enemy activity...")
    elif (e < 0):
         RetroScreen.scrollboxadd("Over target by " + str(abs(e))+ " metres")
    else:   
         RetroScreen.scrollboxadd("Short of target by " + str(abs(e))+ " metres")


btnPlus = Button(mainwin,text = "+",command = onclickPlus)
btnPlus.place(x=retroInputx+80,y=retroInputy)

btnMinus = Button(mainwin,text = "-",command = onclickMinus)
btnMinus.place(x=retroInputx-45,y=retroInputy)

btnFire = Button(mainwin,text = "FIRE!", command = onclickFire)
btnFire.place(x=retroInputx+0,y=retroInputy+80,)

retroangletext = LEDlib.LEDscoreobj(canvas1,retroInputx,retroInputy,angle,"white",4,8*4,2)
elevationlabel = medtext(retroInputx-180,retroInputy-30,"Elevation (in degrees)")

FireInstructionlabel = medtext(retroInputx-330,retroInputy-100,"Choose Elevation and click on Fire")

## draw semicircle for elevation angle

def on_close():
     global RetroScreen, instructionbox, titletext, retroangletext, elevationlabel, FireInstructionlabel
     del RetroScreen
     del instructionbox
     del titletext
     del retroangletext
     del elevationlabel
     del FireInstructionlabel
     mainwin.destroy()

def mykey(event):
    key = event.keysym
    if key in "0123456789":
        RetroScreen.scrollboxadd(key)

mainwin.protocol("WM_DELETE_WINDOW", on_close)
mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()