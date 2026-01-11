# This can also be a non-violent basketball "shoot the hoop game"
# Levels for cannon game: multi-target -> Ammo packs, etc, limited shots, shot wall to break, etc

import math
import sys
import os
import time
import random
from tkinter import * 

sys.path.insert(0, os.path.expanduser("~/Documents"))
import LEDlib

charAA = [(0,0, "#B5B3F5"), (1,0, "#B8860B"), (2,0, "#8B4513"), (3,0, "#8B4513"), (4,0, "#8B4513"), (5,0, "#8B4513"), (6,0, "#B8860B"), (7,0, "#B8860B"), (1,1, "#B8860B"), (2,1, "#B8860B"), (3,1, "#8B4513"), (4,1, "#8B4513"), (5,1, "#8B4513"), (6,1, "#B8860B"), (7,1, "#B8860B"), (1,2, "#FFFFE0"), (2,2, "#FFFFE0"), (3,2, "#FFFFE0"), (4,2, "#FFFFE0"), (5,2, "#FFFFE0"), (6,2, "#FFFFE0"), (7,2, "#FFFFE0"), (0,3, "#FFFF00"), (1,3, "#FFFFE0"), (4,3, "#FFFFE0"), (7,3, "#FFFFE0"), (1,4, "#FFFFE0"), (4,4, "#FFFFE0"), (7,4, "#FFFFE0"), (1,5, "#FFFFE0"), (2,5, "#FFFFE0"), (3,5, "#FFFFE0"), (4,5, "#FFFFE0"), (5,5, "#FFFFE0"), (6,5, "#FFFFE0"), (7,5, "#FFFFE0"), (1,6, "#B8860B"), (2,6, "#B5B3F5"), (3,6, "#B5B3F5"), (4,6, "#B5B3F5"), (5,6, "#B5B3F5"), (6,6, "#FFFF00"), (7,6, "#FFFF00"), (0,7, "#8B4513"), (1,7, "#8B4513"), (2,7, "#8B4513"), (3,7, "#B8860B"), (4,7, "#B8860B"), (5,7, "#B8860B"), (6,7, "#8B4513"), (7,7, "#8B4513")]
charAB = [(2,2, "#FFFF00"), (3,2, "#FFFF00"), (5,2, "#FFFF00"), (0,3, "#FFFF00"), (1,3, "#000000"), (2,3, "#FFFF00"), (3,3, "#000000"), (4,3, "#FFFF00"), (5,3, "#000000"), (6,3, "#FFFF00"), (7,3, "#FFFF00"), (2,4, "#FFFF00"), (3,4, "#FFFF00"), (4,4, "#FFFF00"), (5,4, "#FFFF00"), (6,4, "#FFFF00"), (3,6, "#B5B3F5"), (4,6, "#B5B3F5")]
charGun = [(5,0, "#279627"), (6,0, "#8B4513"), (4,1, "#279627"), (5,1, "#8B4513"), (3,2, "#8B4513"), (4,2, "#8B4513"), (2,3, "#8B4513"), (3,3, "#279627"), (1,4, "#279627"), (2,4, "#8B4513"), (3,4, "#AAAAAA"), (4,4, "#8B4513"), (5,4, "#AAAAAA"), (6,4, "#8B4513"), (0,5, "#AAAAAA"), (1,5, "#8B4513"), (2,5, "#AAAAAA"), (3,5, "#279627"), (4,5, "#AAAAAA"), (5,5, "#8B4513"), (6,5, "#279627"), (7,5, "#8B4513"), (0,6, "#4C3A23"), (1,6, "#000000"), (2,6, "#000000"), (3,6, "#000000"), (4,6, "#000000"), (5,6, "#000000"), (6,6, "#000000"), (7,6, "#4C3A23"), (1,7, "#4C3A23"), (2,7, "#4C3A23"), (3,7, "#4C3A23"), (4,7, "#4C3A23"), (5,7, "#4C3A23"), (6,7, "#4C3A23")]
charBall =  [(3,3, "#AAAAAA"), (4,3, "#FFFFFF"), (3,4, "#DDDDDD"), (4,4, "#AAAAAA")]


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

def sind(x):
    return math.sin(math.radians(x))

def cosd(x):
    return math.cos(math.radians(x))

def tand(x):
    return math.tan(math.radians(x))

def screenx(x): # converts real x position to a screen position
    return int(x*scalex)

def screeny(y): # converts real y position to a screen position
    return int(groundy-y*scaley)

def updateball():
    global ballx0, bally0, vx, vy
    ballx0 = gunx+rgun*cosd(angle)
    bally0 = guny+rgun*sind(angle)
    vx = v*cosd(angle)
    vy = v*sind(angle)
    ball.resetposition(screenx(ballx0), screeny(bally0))

def moveball():
    global ballx, bally, vx, vy
    ballx = ballx + vx*STEPTIME/1000
    bally = bally + vy*STEPTIME/1000
    vy = vy - g*STEPTIME/1000
    ball.resetposition(screenx(ballx), screeny(bally))


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


STEPTIME = 100 # in ms
rgun=300 # radius of gun barrel
angle = 45
scalex = 0.03
scaley = 0.03
retroInputx = 1400
retroInputy = 400
groundy = 800
gunx = 400
guny = 0
g = 9.81
ballx0 = gunx+rgun*cosd(angle) # initial real position of ball
bally0 = guny+rgun*sind(angle)
ballx = ballx0 # ballx, bally is the real math (x,y) position of ball
bally = bally0
#  v^2/g = max range = r
v = math.sqrt(r*g)
vx = v*cosd(angle)
vy = v*sind(angle)
myship = LEDlib.LEDobj(canvas1,10,10,dx = 0,dy = 0,CharPoints=charAA, pixelsize = 2)
myship2 = LEDlib.LEDobj(canvas1,40,10,dx = 0,dy = 0,CharPoints=charAB, pixelsize = 2)
gun = LEDlib.LEDobj(canvas1,screenx(gunx),screeny(guny),dx = 0,dy = 0,CharPoints=charGun, pixelsize = 2)
ball = LEDlib.LEDobj(canvas1,screenx(ballx0),screeny(bally0),dx = 0,dy = 0,CharPoints=charBall, pixelsize = 2)


z = 0
s1 = 0
playeralive = True;

t = int(r*(.1+0.8*random.random())) # distance to target
RetroScreen.scrollboxadd("Distance to target is "+str(t)+" metres")




def onclickPlus():
    global angle
    angle = angle + 1
    if angle > 89: angle = 89
    retroangletext.update(angle)
    updateball()

def onclickMinus():
    global angle
    angle = angle - 1
    if angle < 1: angle = 1
    retroangletext.update(angle)
    updateball()

s = 0
z = 0
def onclickFire():
    global s, z, ballx, bally
    ballx = ballx0
    bally = bally0
    updateball()
    timer1()
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

def timer1():
    moveball()
    if bally >= 0:
       #print(bally)
       mainwin.after(10,timer1)

mainwin.protocol("WM_DELETE_WINDOW", on_close)
mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()