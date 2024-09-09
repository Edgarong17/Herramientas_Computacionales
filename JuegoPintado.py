from turtle import *
from freegames import vector
from math import sqrt

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle2(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    if end.x<start.x:
        posx=start.x-end.x
    else:
        posx=end.x-start.x
    if start.y<end.y:
        posy=start.y - end.y
    else:
        posy=end.y - start.y
    posx=posx*posx
    posy=posy*posy
    radio=sqrt(posx+posy) 
    begin_fill()
    circle(radio)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = abs(end.x - start.x)
    height = abs(end.y - start.y)

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    base = abs(end.x - start.x)

    for count in range(3):
        forward(base)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

def color2(col):
    color(col)
    pencolor(col)
    fillcolor(col)


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('pink'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('#C733FF'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()



