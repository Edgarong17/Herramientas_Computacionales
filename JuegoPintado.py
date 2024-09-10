from turtle import *
from freegames import vector
from math import sqrt

#Crea una linea desde la posicion del primer click hasta el segundo click
def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Se dibuja un cuadrado tomando en cuenta 2 click del mouse
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x) #Se pinta hacia un lado la distancia entre los clicks
        left(90) #Se rota 90 grados 4 veces para que en cada iteracion tenga otra linea el cadrado

    end_fill()

#Se dibuja un circulo tomando la distancia entre los clicks como radio
def circle2(start, end):
    up()
    goto(start.x, start.y) #Vaa la posicion inicial
    down()
    #Se obtiene el cambio en x y y
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
    #Se saca la hipotenusa del triangulo que seria el radio del circulo
    radio=sqrt(posx+posy) 
    begin_fill()
    #Se crea un circulo del radio calculado
    circle(radio)
    end_fill()

#Se dibuja un rectangulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Se calcula el largo y ancho del rectangulo
    width = abs(end.x - start.x)
    height = abs(end.y - start.y)
    #Se crean las lineas del rectangulo
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()

#Se dibuja un triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Se define el largo de la base que sera el utilizado para los lados
    base = abs(end.x - start.x)
    #Se crean las lineas del triangulo
    for count in range(3):
        forward(base)
        left(120)

    end_fill()

#Se guardan los click de inicio y fin y tambien se llaman a las funciones de crear figuras
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

#Se guarda la tecla que se toca, esta se usa para definir que figura se realizara
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Se define lo que hace cada tecla
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



