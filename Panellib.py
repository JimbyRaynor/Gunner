def drawleftbevel(canvas, x=100, y=300,height = 100, width = 10, inner=False):
   points = [
       x,y, # top left
       x+width, y+width, # top right
       x+width, y+height-width, # bottom right
       x, y+height # bottom left 
            ]
   if inner:
     canvas.create_polygon(points, fill ="#585858") 
   else:
     canvas.create_polygon(points, fill ="#DFDFDF")

def drawrightbevel(canvas, x=100, y=300,height = 100, width = 10, inner=False):
   points = [
       x-width,y+width, # top left
       x, y, # top right
       x, y+height, # bottom right
       x-width, y+height-width # bottom left 
            ]
   if not inner:
     canvas.create_polygon(points, fill ="#585858") 
   else:
     canvas.create_polygon(points, fill ="#BFBFBF")

def drawtopbevel(canvas, x=100, y=300,width = 100, bevelsize = 10, inner=False):
   points = [
       x,y, # top left
       x+width, y, # top right
       x+width-bevelsize, y+bevelsize, # bottom right
       x+bevelsize, y+bevelsize # bottom left 
            ]
   if inner:
     canvas.create_polygon(points, fill ="#505050") 
   else:
     canvas.create_polygon(points, fill ="#DFDFDF")  

def drawbottombevel(canvas, x=100, y=300,width = 100, bevelsize = 10, inner=False):
   points = [
       x+bevelsize,y, # top left
       x+width-bevelsize, y, # top right
       x+width, y+bevelsize, # bottom right
       x, y+bevelsize # bottom left 
            ]
   if not inner:
     canvas.create_polygon(points, fill ="#666666") 
   else:
     canvas.create_polygon(points, fill ="#BBBBBB")



def drawpanel(canvas,x,y,width,height,bevelsize):
    points = [
       x,y, # top left
       x+width, y, # top right
       x+width, y+height, # bottom right
       x, y+height# bottom left 
            ]
    canvas.create_polygon(points, fill ="#999999")
    drawleftbevel(canvas,x,y,height,bevelsize) 
    drawrightbevel(canvas,x+width,y,height,bevelsize) 
    drawtopbevel(canvas,x,y,width,bevelsize) 
    drawbottombevel(canvas,x,y+height-bevelsize,width,bevelsize)

def drawpanelinner(canvas,x,y,width,height,bevelsize):
    points = [
       x,y, # top left
       x+width, y, # top right
       x+width, y+height, # bottom right
       x, y+height# bottom left 
            ]
    canvas.create_polygon(points, fill ="#000000")
    drawleftbevel(canvas,x,y,height,bevelsize, inner=True) 
    drawrightbevel(canvas,x+width,y,height,bevelsize, inner=True) 
    drawtopbevel(canvas,x,y,width,bevelsize, inner=True) 
    drawbottombevel(canvas,x,y+height-bevelsize,width,bevelsize, inner=True)
