from turtle import *
from random import randrange, choice
from freegames import square, vector

#Se agregaron los 5 colores que pueden tener
colors = ['blue', 'green', 'yellow', 'pink', 'black']

#Se elige un color aleatorio entre los colores
snake_color = choice(colors)

#Se elige un color aleatorio entre los colores restantes 
food_color = choice([color for color in colors if color != snake_color])

#Se ponen las posiciones iniciales y el movimiento inicial
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#La velocidad de la serpiente
vel = 10

#Define la velocidad y la dirrecion en la que se desplaza la serpiente
def change(x, y):
    "Change snake direction." 
    aim.x = x
    aim.y = y

#Busca si la serpiente ha salido del tablero o no
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Mueve a la serpiente y a las frutas
def move():
    global vel
    head = snake[-1].copy()
    head.move(aim)
    #Se actualiza la cabeza de la serpiente y se checa si choca
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    #Se agrega una nueva cabeza
    snake.append(head)
    #Variables para checar si la cabeza esta cerca de la fruta
    compx=head.x -food.x
    compy=head.y - food.y
    #en caso de que la serpiente se coma la fruta
    if compx<=5 and compx>=-5 and compy<=5 and compy>=-5:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10 #Se mueve aleatoriamente la fruta
        food.y = randrange(-15, 15) * 10
        vel = vel+1 #Se aumenta la velocidad
    else:
        snake.pop(0) #Se quita la ultima parte del cuerpo de la serpiente
        if food.x + 1 >=190: #Se mueve de forma aleatoria la comida
            food.x = randrange(food.x-1, food.x)
        elif food.x -1 <= -200:
            food.x = randrange(food.x, food.x+1)
        else:
            food.x = randrange(food.x-1, food.x+1)

        if food.y + 1 >=190:
            food.y = randrange(food.y-1,food.y)
        elif food.y -1 <= -200:
            food.y = randrange(food.y, food.y+1)
        else:
            food.y = randrange(food.y-1, food.y+1)


    clear()
    #Se ponen cuadrados para cada parte del cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)
    #Se pone un cuadrado para la comida
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(vel, 0), 'Right')
onkey(lambda: change(-vel, 0), 'Left')
onkey(lambda: change(0, vel), 'Up')
onkey(lambda: change(0, -vel), 'Down')
move()

done()

