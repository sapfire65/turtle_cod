import turtle  # Подключаем модуль turtle
import random

turtle.speed(0) # Скорость отрисовки

# Рисуем клубок
def point_1(count):
    for i in range(count + 1):
        color_v = ['blue', 'red', 'yellow', 'green', 'orange', 'pink', 'brown', 'violet']
        random_i = random.randrange(start=0, stop=7)
        turtle.color(color_v[random_i])
        turtle.width(i // 60)
        turtle.forward(i + 2)
        turtle.left(i + 3)

# Отступ 1
def go_to_p(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
# Отступ 2
def otstup(x, y):
    turtle.up()
    turtle.goto(x, y)

# Рисуем шедевр абстракционизма
point_1(175)   # 1

go_to_p(300, 30)

point_1(175) # 2

go_to_p(-250, 190)

point_1(175) # 3

go_to_p(-450, 330)

point_1(175) # 4

# отводим черепашку
turtle.up()
turtle.forward(200)
turtle.left(80)

# Пишем -  ZontiQ
def zontiq():
    # turtle.speed(3)
    turtle.down()
    turtle.right(75)
    turtle.up()
    turtle.goto(-450, -30)

 # буквы
    def z_1():
        color_v = ['blue', 'red', 'yellow', 'green', 'orange', 'pink', 'brown', 'violet', 'bleak']
        random_i = random.randrange(start=0, stop=8)
        turtle.color(color_v[random_i])

        turtle.down()
        turtle.forward(100)
        turtle.right(140)
        turtle.forward(130)
        turtle.left(140)
        turtle.forward(110)

    def o_1(r):
        color_v = ['blue', 'red', 'yellow', 'green', 'orange', 'pink', 'brown', 'violet']
        random_i = random.randrange(start=0, stop=7)
        turtle.color(color_v[random_i])
        turtle.down()
        turtle.circle(r)

    def n_1():
        color_v = ['blue', 'red', 'yellow', 'green', 'orange', 'pink', 'brown', 'violet']
        random_i = random.randrange(start=0, stop=7)
        turtle.color(color_v[random_i])
        turtle.down()
        turtle.forward(20)  # рисует
        turtle.left(90) # поворот на n градусов
        turtle.forward(50)
        turtle.right(140)
        turtle.forward(65)
        turtle.left(45)
        turtle.forward(20)
        turtle.left(95)
        turtle.forward(90)  # правая сторона
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(140)
        turtle.forward(65)
        turtle.left(50)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(90) # левая сторона

    def t_1():
        color_v = ['blue', 'red', 'yellow', 'green', 'orange', 'pink', 'brown', 'violet']
        random_i = random.randrange(start=0, stop=7)
        turtle.color(color_v[random_i])
        turtle.up()
        turtle.forward(150)
        turtle.left(90)
        turtle.down()
        turtle.forward(110) # Высота буквы
        turtle.left(90)
        turtle.forward(310)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(110) # Высота буквы
        turtle.right(90)
        turtle.forward(20)
        turtle.right(180)
        turtle.up()


# Пишем инструкции для Z
    for i in range(1, 30):
        turtle.width(i // 3)
        otstup(-400 - (-4 + i*2), -50 - -(i*2))
        turtle.color('blue')
        z_1()

# Пишем инструкции для O
    for j in range(11):
        turtle.width(j // 2)
        otstup(-200  - j*2, -125 - j*2)
        o_1(40)

# Пишем инструкции для N
    for n in range(15):
        turtle.width(n // 3)
        otstup(-100 + - n*2, -125 + - n*2)
        n_1()
        turtle.left(90)

# Пишем инструкции для T
    for t in range(7):
        turtle.width(t // 2)
        otstup(-100 + - t * 2, -125 + - t * 2)
        t_1()

zontiq()
turtle.exitonclick()
