import math

# TODO
# Make load/save easier

psize = 3
charwidth = 23

ONE = [(1,6), (2,1), (2,6), (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (5,6), (6,6)]
ZERO = [(0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,2), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,1), (6,2), (6,3), (6,4), (6,5)]
TWO = [(0,1), (1,0), (1,1), (1,2), (1,6), (2,0), (2,2), (2,5), (2,6), (3,0), (3,4), (3,5), (3,6), (4,0), (4,4), (4,6), (5,0), (5,1), (5,2), (5,3), (5,6), (6,1), (6,2), (6,3), (6,5), (6,6)]
THREE = [(0,1), (0,5), (1,0), (1,1), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,1), (6,2), (6,4), (6,5)]
FOUR = [(0,3), (0,4), (1,2), (1,3), (1,4), (2,1), (2,2), (2,4), (3,0), (3,1), (3,4), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,4)]
FIVE = [(0,0), (0,1), (0,2), (0,3), (0,5), (1,0), (1,1), (1,2), (1,3), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,4), (6,5)]
SIX = [(0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,3), (5,4), (5,5), (5,6), (6,1), (6,4), (6,5)]
SEVEN = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,5), (2,6), (3,0), (3,3), (3,4), (3,5), (3,6), (4,0), (4,1), (4,2), (4,3), (4,4), (5,0), (5,1), (5,2), (6,0), (6,1)]
EIGHT = [(0,1), (0,2), (0,4), (0,5), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,1), (6,2), (6,4), (6,5)]
NINE = [(0,1), (0,2), (0,5), (1,0), (1,1), (1,2), (1,3), (1,5), (1,6), (2,0), (2,3), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,5), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (6,1), (6,2), (6,3), (6,4)]

PLUS = [(1,3), (2,3), (3,1), (3,2), (3,3), (3,4), (3,5), (4,3), (5,3)]
TIMES = [(1,1), (1,5), (2,2), (2,4), (3,3), (4,2), (4,4), (5,1), (5,5)]
LEFTBRACKET = [(2,2), (2,3), (2,4), (3,1), (3,5), (4,0), (4,6)]
RIGHTBRACKET = [(2,0), (2,6), (3,1), (3,5), (4,2), (4,3), (4,4)]
EQUALS = [(1,2), (1,4), (2,2), (2,4), (3,2), (3,4), (4,2), (4,4), (5,2), (5,4), (6,2), (6,4)]

# leave rightmost column blank
# leave bottom row blank  
charA = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (4,0), (4,3), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charB = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,1), (6,2), (6,4), (6,5)]
charC = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,6), (4,0), (4,6), (5,0), (5,1), (5,5), (5,6), (6,0), (6,1), (6,5), (6,6)]
charD = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,6), (4,0), (4,1), (4,6), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,2), (6,3), (6,4), (6,5)]
charE = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,6), (6,0), (6,1), (6,5), (6,6)]
charF = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (4,0), (4,3), (5,0), (6,0)]
charG = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,3), (6,4), (6,5), (6,6)]
charH = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (4,3), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charI = [(2,0), (2,6), (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (5,0), (5,6)]
charJ = [(1,5), (1,6), (2,5), (2,6), (3,0), (3,6), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0)]
charK = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,2), (3,3), (3,4), (4,1), (4,2), (4,4), (4,5), (5,0), (5,1), (5,5), (5,6), (6,0), (6,6)]
charL = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,6), (4,6), (5,6), (6,5), (6,6)]
charM = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,1), (2,2), (3,2), (3,3), (4,1), (4,2), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charN = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,2), (3,3), (4,3), (4,4), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charO = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,6), (4,0), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charP = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (4,0), (4,3), (5,0), (5,1), (5,2), (5,3), (6,0), (6,1), (6,2), (6,3)]
charQ = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,6), (4,0), (4,5), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (7,7)]
charR = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,0), (3,3), (3,4), (4,0), (4,3), (4,4), (4,5), (5,0), (5,1), (5,2), (5,3), (5,5), (5,6), (6,1), (6,2), (6,6)]
charS = [(1,0), (1,1), (1,2), (1,3), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,5), (2,6), (3,0), (3,3), (3,6), (4,0), (4,3), (4,6), (5,0), (5,1), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,3), (6,4), (6,5), (6,6)]
charT = [(1,0), (2,0), (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (5,0), (6,0)]
charU = [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (3,6), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charV = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (2,6), (3,5), (3,6), (4,3), (4,4), (4,5), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (6,0), (6,1), (6,2), (6,3)]
charW = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,4), (2,5), (3,3), (3,4), (4,4), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
charX = [(1,0), (1,1), (1,5), (1,6), (2,0), (2,1), (2,2), (2,4), (2,5), (2,6), (3,2), (3,3), (3,4), (4,2), (4,3), (4,4), (5,0), (5,1), (5,2), (5,4), (5,5), (5,6), (6,0), (6,1), (6,5), (6,6)]
charY = [(1,0), (1,1), (2,0), (2,1), (2,2), (3,2), (3,3), (3,4), (3,5), (3,6), (4,2), (4,3), (4,4), (4,5), (4,6), (5,0), (5,1), (5,2), (6,0), (6,1)]
charZ = [(1,0), (1,1), (1,5), (1,6), (2,0), (2,4), (2,5), (2,6), (3,0), (3,3), (3,4), (3,6), (4,0), (4,2), (4,3), (4,6), (5,0), (5,1), (5,2), (5,6), (6,0), (6,1), (6,5), (6,6)]
charPercent = [(1,0), (1,1), (1,5), (2,0), (2,1), (2,4), (3,3), (4,2), (4,5), (4,6), (5,1), (5,5), (5,6)]
charDot = [(3,5), (3,6), (4,5), (4,6)]
charColon = [(3,1), (3,2), (3,5), (3,6), (4,1), (4,2), (4,5), (4,6)]
charQuestionMark = [(1,1), (2,0), (3,0), (3,4), (3,6), (4,0), (4,3), (5,1), (5,2)]

def createLED(canvas, x,y, LEDpoints):
 p1 = canvas.create_rectangle(x, y, x+psize, y+psize, fill="black")
 p2 = canvas.create_oval(x, y, x+psize, y+psize, fill="white")
 LEDpoints.append(p1)
 LEDpoints.append(p2)

def createLEDcolour(canvas, x,y, colour, LEDpoints, square=False):
 p1 = canvas.create_rectangle(x, y, x+psize, y+psize, fill="black")
 if square == False:
    p2 = canvas.create_oval(x, y, x+psize, y+psize, fill=colour)
 else:
    p2 = canvas.create_rectangle(x, y, x+psize-1, y+psize-1, fill=colour)
 #p2 = canvas.create_rectangle(x, y, x+psize-1, y+psize-1, fill=colour)
 LEDpoints.append(p1)
 LEDpoints.append(p2)

def createLEDcolourSolid(canvas, x,y, colour, LEDpoints):
 p2 = canvas.create_rectangle(x, y, x+psize, y+psize, fill=colour, outline = "")
 LEDpoints.append(p2)

# white char
def createChar(canvas,x,y,points, LEDpoints):
  prect = canvas.create_rectangle(x, y, x+psize*8, y+psize*8, fill="black") # erase background for new char
  LEDpoints.append(prect)
  for p in points:
    createLED(canvas,x+p[0]*psize,y+p[1]*psize, LEDpoints)

# All one colour char
def createCharBlockColour(canvas,x,y,colour, points, LEDpoints):
  prect = canvas.create_rectangle(x, y, x+psize*8, y+psize*8, fill="black") # erase background for new char
  LEDpoints.append(prect)
  for p in points:
    createLEDcolour(canvas,x+p[0]*psize,y+p[1]*psize, colour, LEDpoints) 

def createCharBlockColour2(canvas,x,y,colour, points, LEDpoints,solid=False, bg= True, square=False):
  if bg == True:
    prect = canvas.create_rectangle(x, y, x+psize*8, y+psize*8, fill="black") # erase background for new char
    LEDpoints.append(prect)
  for p in points:
    if solid == True:
       createLEDcolourSolid(canvas,x+p[0]*psize,y+p[1]*psize, colour, LEDpoints)
    else:
       createLEDcolour(canvas,x+p[0]*psize,y+p[1]*psize, colour, LEDpoints, square=square) 

def pygamecreateCharBlockColour2(screen,x,y,colour, points,solid=False):
    for p in points:
      if solid == True:
       srect = pygame.Rect(x+p[0]*psize,y+p[1]*psize, psize, psize)
       pygame.draw.rect(screen, colour, srect)
      else:
       pygame.draw.circle(screen,colour,(x+p[0]*psize+psize/2,y+p[1]*psize+psize/2),psize/2)

  
# Multi-Colour char
def createCharColour(canvas,x,y,colourpoints, LEDpoints):
  for p in colourpoints:
    createLEDcolour(canvas,x+p[0]*psize,y+p[1]*psize,p[2], LEDpoints)

def createCharColourSolid(canvas,x,y,colourpoints, LEDpoints):
  for p in colourpoints:
    createLEDcolourSolid(canvas,x+p[0]*psize,y+p[1]*psize,p[2], LEDpoints)
  
def pixelline(canvas,x,y,dx,dy,n,colour, LEDpoints):
   for i in range(n):
       createLEDcolour(canvas, x+i*dx*psize,y+i*dy*psize,colour, LEDpoints)

def pixellinedouble(canvas,x,y,dx,dy,n,colour, LEDpoints):
   for i in range(n):
       createLEDcolour(canvas, x+i*dx*psize,y+i*dy*psize,colour, LEDpoints)
       createLEDcolour(canvas, x+i*dx*psize+dy*psize,y+i*dy*psize+dx*psize,colour, LEDpoints)

def pixellinetriple(canvas,x,y,dx,dy,n,colour, LEDpoints):
   for i in range(n):
       createLEDcolour(canvas, x+i*dx*psize,y+i*dy*psize,colour, LEDpoints)
       createLEDcolour(canvas, x+i*dx*psize+dy*psize,y+i*dy*psize+dx*psize,colour, LEDpoints)
       createLEDcolour(canvas, x+i*dx*psize+2*dy*psize,y+i*dy*psize+2*dx*psize,colour, LEDpoints)
          

# From Copilot: enumerate is a built-in Python function that makes iteration more convenient when you need both 
# an index and the value of an iterable (like a list or string).
def ShowText(canvas,x,y,mytext, LEDpoints):
    charactermap = [charA,charB,charC,charD,charE,charF,charG,charH,charI,charJ,charK,charL,charM,charN,charO,charP,charQ,charR,charS,charT,charU,charV,charW,charX,charY,charZ] 
    for i,c in enumerate(mytext):  # i=0 pairs with c = first char in mytext, i = 1 pairs with c = second char, etc
       createChar(canvas,x+i*charwidth,y,charactermap[ord(c)-65], LEDpoints)

def ShowScore(canvas,x,y,myscore, LEDpoints,numzeros=9):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    stringscore = str(myscore).zfill(numzeros) 
    for i,c in enumerate(stringscore):
       createChar(canvas,x+i*charwidth,y,digits[int(c)], LEDpoints)

def ShowColourScore(canvas,x,y,colour, myscore, LEDpoints,numzeros=9):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    stringscore = str(myscore).zfill(numzeros) 
    for i,c in enumerate(stringscore):
       createCharBlockColour(canvas,x+i*charwidth,y,colour,digits[int(c)], LEDpoints)

def ShowColourScore2(canvas,x,y,colour, myscore, LEDpoints,numzeros=9,solid=False,bg=True):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    stringscore = str(myscore).zfill(numzeros) 
    for i,c in enumerate(stringscore):
       createCharBlockColour2(canvas,x+i*charwidth,y,colour,digits[int(c)], LEDpoints, solid = solid, bg = bg)

def pygameShowColourScore2(canvas,x,y,colour, myscore,numzeros=9,solid=False):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    stringscore = str(myscore).zfill(numzeros) 
    for i,c in enumerate(stringscore):
       pygamecreateCharBlockColour2(canvas,x+i*charwidth,y,colour,digits[int(c)], solid = solid)

def ShowColourText(canvas,x,y,colour, mytext, LEDpoints):
    charactermap = [charA,charB,charC,charD,charE,charF,charG,charH,charI,charJ,charK,charL,charM,charN,charO,charP,charQ,charR,charS,charT,charU,charV,charW,charX,charY,charZ] 
    for i,c in enumerate(mytext):  # i=0 pairs with c = first char in mytext, i = 1 pairs with c = second char, etc
       createCharBlockColour(canvas,x+i*charwidth,y,colour, charactermap[ord(c)-65], LEDpoints)  

def ShowColourText2(canvas,x,y,colour, mytext, LEDpoints, solid = False, bg = True, multicolour = False, plusorder = ["green","green"], square=False):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    mytext = mytext.upper()
    AdjustPos = 0
    PlusCount = 0
    charactermap = [charA,charB,charC,charD,charE,charF,charG,charH,charI,charJ,charK,charL,charM,charN,charO,charP,charQ,charR,charS,charT,charU,charV,charW,charX,charY,charZ] 
    for i,c in enumerate(mytext):  # i=0 pairs with c = first char in mytext, i = 1 pairs with c = second char, etc
       if c in ["M","W","V"]:
           AdjustPos =  AdjustPos + charwidth/8
       if c in "I()":
           AdjustPos =  AdjustPos - charwidth/8
       if c != ' ':
          if c in "0123456789":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,digits[int(c)], LEDpoints, solid = solid, bg = bg, square=square)
          elif c == "%":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charPercent, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == ".":
            AdjustPos = AdjustPos-2*charwidth/8
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charDot, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == ":":
            AdjustPos = AdjustPos-2*charwidth/8
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charColon, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == "+":
            newcolour = colour
            if multicolour:
               if PlusCount < len(plusorder):
                  newcolour = plusorder[PlusCount]
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,newcolour,PLUS, LEDpoints, solid = solid, bg = bg, square=square)
            PlusCount = PlusCount + 1
          elif c == "*":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,TIMES, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == "?":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charQuestionMark, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == "(":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,LEFTBRACKET, LEDpoints, solid = solid, bg = bg, square=square)
          elif c == ")":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,RIGHTBRACKET, LEDpoints, solid = solid, bg = bg, square=square)
          elif c== "=":
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,EQUALS, LEDpoints, solid = solid, bg = bg, square=square) 
          elif ord(c)-65 >= 0 and ord(c)-65 < len(charactermap):
            createCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour, charactermap[ord(c)-65], LEDpoints, solid = solid, bg = bg, square=square)  
       if c in "I()":
           AdjustPos =  AdjustPos - charwidth/8  

def pygameShowColourText2(canvas,x,y,colour, mytext, solid = False):
    digits = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
    mytext = mytext.upper()
    AdjustPos = 0
    charactermap = [charA,charB,charC,charD,charE,charF,charG,charH,charI,charJ,charK,charL,charM,charN,charO,charP,charQ,charR,charS,charT,charU,charV,charW,charX,charY,charZ] 
    for i,c in enumerate(mytext):  # i=0 pairs with c = first char in mytext, i = 1 pairs with c = second char, etc
       if c in ["M","W","V"]:
           AdjustPos =  AdjustPos + charwidth/8
       if c in ["I"]:
           AdjustPos =  AdjustPos - charwidth/8
       if c != ' ':
          if c in "0123456789":
            pygamecreateCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,digits[int(c)], solid = solid)
          elif c == "%":
            pygamecreateCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charPercent, solid = solid)
          elif c == ".":
            AdjustPos = AdjustPos-2*charwidth/8
            pygamecreateCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charDot, solid = solid)
          elif c == ":":
            AdjustPos = AdjustPos-2*charwidth/8
            pygamecreateCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour,charColon, solid = solid)
          elif ord(c)-65 >= 0 and ord(c)-65 < len(charactermap):
            pygamecreateCharBlockColour2(canvas,x+i*charwidth+AdjustPos,y,colour, charactermap[ord(c)-65], solid = solid)  
       if c in ["I"]:
           AdjustPos =  AdjustPos - charwidth/8    


def Erasepoints(canvas,LEDpoints):
    for p in LEDpoints:
      canvas.delete(p)


class LEDtextobj:
    def __init__(self, canvas,x=0,y=0, text = "", colour = "white", pixelsize = 2, charwidth=23, solid = False, bg = False, multicolour = False, plusorder = ["green","green"],square=False):
         self.x = x
         self.y = y
         self.text = text
         self.canvas = canvas
         self.LEDPoints = []
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.solid = solid
         self.bg = bg
         self.multicolour = multicolour
         self.plusorder = plusorder
         self.square = square
         self.draw()
    def __del__(self): # the destructor 
        self.undraw()
    def draw(self):
        global charwidth, psize
        self.undraw()
        charwidth = self.charwidth
        psize = self.pixelsize
        ShowColourText2(self.canvas,self.x,self.y,self.colour,self.text,self.LEDPoints, self.solid, self.bg, self.multicolour, self.plusorder, self.square) 
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
         self.LEDPoints.clear()
    def update(self,mytext):
        self.text = mytext
        self.draw()


class scrollboxobj:
    def __init__(self, canvas,x=0,y=0,width=1000,height=700):
        self.x = x
        self.y = y
        self.maxlines = 20
        self.width = width
        self.height = height
        self.canvas = canvas
        self.walls = 0
        self.scrollboxtext = [] # list of lines of text to display
        self.scrollboxLEDlines = [] # list of canvas objects that draw each line of text
        self.scrollboxstart = 0 # draw lines starting at line scrollboxstart (simulates scrolling)
        for i in range(self.maxlines):
            self.scrollboxLEDlines.append(self.mediumtext(self.x+5,self.y+5+i*26," "))
        self.draw()
    def __del__(self):  # this will call the destructor of all objects inside this class, e.g. scrollboxLEDlines and all its contents
        self.undraw()
    def mediumtext(self,x,y,mytext):
        return LEDtextobj(self.canvas,x=x,y=y,text=mytext,colour="light green",pixelsize = 3, charwidth=8*3 , solid = False, square=False)
    def scrollboxset(self,i,mytext):
        self.scrollboxLEDlines[i].update(mytext)
    def scrollboxadd(self,mytext):
        if len(self.scrollboxtext) >= self.maxlines: self.scrollboxstart = self.scrollboxstart + 1
        self.scrollboxtext.append(mytext)
        i = 0
        while i <= self.maxlines and i <= len(self.scrollboxtext)-1-self.scrollboxstart:
          self.scrollboxset(i,self.scrollboxtext[self.scrollboxstart+i])
          i = i + 1
    def draw(self):
        self.walls = self.canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,outline="light green")
    def undraw(self):
        self.canvas.delete(self.walls)

class scrollboxsmallobj:
    def __init__(self, canvas,x=0,y=0,width=1000,height=700):
        self.x = x
        self.y = y
        self.maxlines = 30
        self.width = width
        self.height = height
        self.canvas = canvas
        self.walls = 0
        self.scrollboxtext = [] # list of lines of text to display
        self.scrollboxLEDlines = [] # list of canvas objects that draw each line of text
        self.scrollboxstart = 0 # draw lines starting at line scrollboxstart (simulates scrolling)
        for i in range(self.maxlines):
            self.scrollboxLEDlines.append(self.smalltext(self.x+5,self.y+5+i*20," "))
    def smalltext(self,x,y,mytext):
        return LEDtextobj(self.canvas,x=x,y=y,text=mytext,colour="light green",pixelsize = 2, charwidth=8*2-2, solid = False, square=False)
    def scrollboxset(self,i,mytext):
        self.scrollboxLEDlines[i].update(mytext)
    def scrollboxadd(self,mytext):
        if len(self.scrollboxtext) >= self.maxlines: self.scrollboxstart = self.scrollboxstart + 1
        self.scrollboxtext.append(mytext)
        i = 0
        while i <= self.maxlines and i <= len(self.scrollboxtext)-1-self.scrollboxstart:
          self.scrollboxset(i,self.scrollboxtext[self.scrollboxstart+i])
          i = i + 1


class pygameLEDtextobj:
    def __init__(self, screen,x=0,y=0, text = "", colour = "white", pixelsize = 2, charwidth=23, solid = False):
         self.x = x
         self.y = y
         self.text = text
         self.screen = screen
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.solid = solid
         self.draw()
    def draw(self):
        global charwidth, psize
        charwidth = self.charwidth
        psize = self.pixelsize
        pygameShowColourText2(self.screen,self.x,self.y,self.colour,self.text, self.solid) 
    def update(self,mytext):
        self.text = mytext
        self.draw()

class pygameLEDscoreobj:
    def __init__(self, screen,x=0,y=0, score = 0, colour = "white", pixelsize = 2, charwidth=23, numzeros = 0, solid = False):
         self.x = x
         self.y = y
         self.score = score
         self.screen = screen
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.numzeros = numzeros 
         self.solid = solid
         self.draw()
    def draw(self):
        global psize, charwidth
        charwidth = self.charwidth
        psize = self.pixelsize
        pygameShowColourScore2(self.screen,self.x,self.y,self.colour,self.score, self.numzeros, self.solid) 
    def update(self,myscore):
        self.score = myscore
        self.draw()

def rotatepoints(points,angle,center):
         newpoints = []
         anglerad = math.radians(angle)
         cx,cy = center
         for x,y,z in points:
              x = x - cx
              y = y - cy
              newx = x* math.cos(anglerad)- y*math.sin(anglerad) + cx
              newy = x * math.sin(anglerad) + y*math.cos(anglerad) + cy
              newpoints.append((newx,newy,z))
         return newpoints

class LEDobj:
    def __init__(self, canvas,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2, typestring = "unknown"):
         global psize
         self.alive = True
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.canvas = canvas
         self.typestring = typestring
         self.LEDPoints = []
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.PointsType = 0
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.CollisionPoints = [(0,0,0)]
         self.RotatedCollisionPoints = [(0,0,0)]
         self.collisionimage = 0
         self.collisionlinesimage = 0
         self.collisionrectshow = False
         self.collisionlinesshow = False
         self.pixelsize = pixelsize
         psize = self.pixelsize
         createCharColourSolid(canvas,x,y,CharPoints,self.LEDPoints)
    def resetposition(self,x,y):
        self.x, self.y = x,y
        self.dx, self.dy = 0,0
        self.draw()
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
         self.LEDPoints.clear()
    def draw(self):
        global psize
        self.undraw()
        psize = self.pixelsize
        createCharColourSolid(self.canvas,self.x,self.y,self.CharPoints,self.LEDPoints)
        if self.collisionlinesshow:
           self.canvas.delete(self.collisionlinesimage)
           self.showcollisionlines()
        if self.collisionrectshow:
              self.canvas.delete(self.collisionimage)
              self.showcollisionrect()
    def move(self): 
         self.x = self.x + self.dx
         self.y = self.y + self.dy
         self.draw()
    def rotate(self,angledeg):
         centerx = sum(x for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         centery = sum(y for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         self.CharPoints = rotatepoints(self.OriginalCharPoints,angle=angledeg,center=(centerx,centery))
         self.RotatedCollisionPoints = rotatepoints(self.CollisionPoints,angle=angledeg,center=(centerx,centery))
         self.draw()
    def showcollisionrect(self):
         self.collisionrectshow = True
         x1,y1,x2,y2 = self.collisionrect 
         self.collisionimage = self.canvas.create_rectangle(self.x+x1,self.y+y1,self.x+x2,self.y+y2,fill="", outline = "white") 
    def showcollisionlines(self):
         self.collisionlinesshow = True
         flatpoints = []
         for x,y,z in self.RotatedCollisionPoints:
            x1 = x*self.pixelsize + self.x
            y1 = y*self.pixelsize + self.y
            flatpoints.append((x1,y1))
         self.collisionlinesimage = self.canvas.create_polygon(flatpoints, outline="white", width=2)

class LEDscoreobj:
    def __init__(self, canvas,x=0,y=0, score = 0, colour = "white", pixelsize = 2, charwidth=23, numzeros = 0, solid = False, bg = True):
         self.x = x
         self.y = y
         self.score = score
         self.canvas = canvas
         self.LEDPoints = []
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.numzeros = numzeros 
         self.solid = solid
         self.bg = bg
         self.draw()
    def draw(self):
        global psize, charwidth
        self.undraw()
        charwidth = self.charwidth
        psize = self.pixelsize
        ShowColourScore2(self.canvas,self.x,self.y,self.colour,self.score,self.LEDPoints, self.numzeros, self.solid, self.bg) 
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
         self.LEDPoints.clear()
    def update(self,myscore):
        self.score = myscore
        self.draw()

