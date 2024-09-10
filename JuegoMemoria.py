from random import *
from turtle import *
from freegames import path

car = path('car.gif')

flags = ["AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "MX", "NL", "NO", "PT", "US", "JP", "IT", "GB",
         "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "GB", "IT", "JP", "MX", "NL", "NO", "PT", "US",
	 "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "MX", "NL", "NO", "PT", "US", "JP", "IT", "GB",
         "AR", "AU", "BR", "CA", "CN", "DE", "ES", "FR",
         "GB", "IT", "JP", "MX", "NL", "NO", "PT", "US"]

state = {'mark': None}
hide = [True] * 64
NTaps=0


def square(x, y):
    "Dibuja un cuadrado blanco con un borde negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) en un índice de la lista de casillas."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte un índice de la lista de casillas en coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y las casillas ocultas según el toque del usuario."
    NTaps=NTaps+1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or flags[mark] != flags[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Dibuja la imagen del carro y las casillas."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 8)
        color('black')
        write(flags[mark], align="center", font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(flags)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

