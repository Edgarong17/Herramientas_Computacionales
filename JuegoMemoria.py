#Se importan las librerias principales
from random import *
from turtle import *
from freegames import path

car = path('car.gif')

#Se crearon las cartas para el juego con nombres de paises
flags = ["AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "MX", "NL", "NO", "PT", "US", "JP", "IT", "GB",
         "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "GB", "IT", "JP", "MX", "NL", "NO", "PT", "US",
	 "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "MX", "NL", "NO", "PT", "US", "JP", "IT", "GB",
         "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "GB", "IT", "JP", "MX", "NL", "NO", "PT", "US"]

#Identificador de si la carta ya fue encontrada
state = {'mark': None}
hide = [True] * 64

#Contadores de taps y de cartas abiertas
NTap = 0
COpen= 0

#Crea el tablero con los vordes
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


#Toma las cordenadas del click e identifica la tarjeta en esa casilla
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Convierte el indice de las casillas en cordenadas
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    #Se agrega 1 al contador de taps
    global NTap
    global COpen
    NTap= NTap+1
    spot = index(x, y)
    mark = state['mark']
    #Se identifica si ya existe una casilla marcada y si las tarjetas son igules
    if mark is None or mark == spot or flags[mark] != flags[spot]:
        state['mark'] = spot #Se marca la nueva casilla
    else:
        #Se marcan las tarjetas como encontradas
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        COpen=COpen+2

def draw():
    #Muestra los elementos graficos
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    #Se muestran las tarjetas
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    #Se muestra el numero de la tarjeta tocada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 8)
        color('black')
        write(flags[mark], align="center", font=('Arial', 20, 'normal')) #Se muestra el numero
    up()
    setpos (170, 150)
    write(str(NTap), align = "center", font=('Arial', 12, 'normal')) #Se pone en la esquina superior el numero de taps
    if COpen >= 64:
        setpos (00, 00)
        write("Terminaste el Juego", align = "center",font=('Arial', 18, 'normal')) #Cuando se descubren todas las tarjetas muestra un mensaje de fin
    update() 
    ontimer(draw, 100) #se llama la funcion dependiendo del tiempo transcurrido

shuffle(flags)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap) #Se llama tap cuando se hace un click en la pantalla
draw()
done()

