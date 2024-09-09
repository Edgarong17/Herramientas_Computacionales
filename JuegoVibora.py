from turtle import *
from random import randrange, choice
from freegames import square, vector


colors = ['blue', 'green', 'yellow', 'pink', 'black']


snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction." 
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  #
        update()
        return

    snake.append(head)
    compx=head.x -food.x
    compy=head.y - food.y
    if compx<=5 and compx>=-5 and compy<=5 and compy>=-5:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        if food.x + 1 >=190:
            food.x = randrange(food.x-1,food.x)
        elif food.x -1 <= -200:
            food.x = randrange(food.x,food.x+1)
        else:
            food.x = randrange(food.x-1, food.x+1)

        if food.y + 1 >=190:
            food.y = randrange(food.y-1,food.y)
        elif food.y -1 <= -200:
            food.y = randrange(food.y,food.y+1)
        else:
            food.y = randrange(food.y-1, food.y+1)


    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()

done()

