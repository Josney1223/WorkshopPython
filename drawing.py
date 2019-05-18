import turtle
import time

turtle = turtle.Turtle()
turtle.speed(1)
turtle.color("red")
turtle.fillcolor("blue")

# Quadrado
def Square():
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    x = 5

# Circle
def Circle():
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

# Hexágono
def Hex():
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(50)
        turtle.left(60)
    turtle.end_fill()

# Octógono
def Octo():
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(50)
        turtle.left(45)
    turtle.end_fill()

# Estrela
def Star():
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(150)
    turtle.pendown()
    for i in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.end_fill()

# Estrela Pontuda
def EdgeStar():
    turtle.speed(1)
    for i in range(11):
        xFrom = 0
        yFrom = (10-i) * 20
        xTo = i * 20
        yTo = 0
        turtle.penup()
        turtle.goto(xFrom, yFrom)
        turtle.pendown()
        turtle.goto(xTo, yTo)

    for i in range(11):
        xFrom = (10-i) * 20
        yFrom = 0
        xTo = 0
        yTo = - (i * 20)
        turtle.penup()
        turtle.goto(xFrom, yFrom)
        turtle.pendown()
        turtle.goto(xTo,yTo)

    for i in range(11):
        xFrom = 0
        yFrom = - (10-i) * 20
        xTo = - (i * 20)
        yTo = 0
        turtle.penup()
        turtle.goto(xFrom, yFrom)
        turtle.pendown()
        turtle.goto(xTo,yTo)

    for i in range(11):
        xFrom = - (10-i) * 20
        yFrom = 0
        xTo = 0
        yTo = (i * 20)
        turtle.penup()
        turtle.goto(xFrom, yFrom)
        turtle.pendown()
        turtle.goto(xTo,yTo)

# Batimento Cardíaco
def HeartBeat(lenght):
    xStart = 0
    yStart = 0
    yMaxUp = lenght/4
    yMaxDown = -lenght/4

    turtle.speed(1)
    turtle.pendown()
    turtle.goto(lenght*9/24, 0)

    turtle.speed(3)
    turtle.goto(lenght*11/24, yMaxUp)
    turtle.goto(lenght*13/24, yMaxDown)
    turtle.goto(lenght*15/24, 0)

    turtle.speed(1)
    turtle.goto(lenght, 0)
    turtle.penup()

    turtle.speed(10)
    turtle.goto(xStart, yStart)
    turtle.clear()

# Desenhar Relógio
def Clock(hora, minutos, radius):
    turtle.speed(10)
    xStart = 0
    yStart = 0
    turtle.penup()
    
    # Circulo
    turtle.right(90)
    turtle.forward(radius + radius/10)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(radius + radius/10)
    turtle.penup()
    turtle.goto(xStart, yStart)

    # Pontos das horas
    for i in range(12):
        turtle.forward(radius)
        turtle.pendown()
        turtle.forward(radius/15)
        turtle.stamp()
        turtle.penup()
        turtle.goto(xStart, yStart)
        turtle.left(30)
    
    # Desenhar as horas
    turtle.left(90)
    turtle.right(30*hora)
    turtle.pendown()
    turtle.forward(radius/2)
    turtle.stamp()
    turtle.penup()
    turtle.goto(xStart, yStart)
    turtle.left(30*hora)
    turtle.right(minutos*6)
    turtle.pendown()
    turtle.forward(radius*3/4)
    turtle.penup()
    turtle.goto(xStart, yStart)

# Cinema
def MovieTheater():
    room = []
    for i in range(19):
        room.append([i])
        for j in range(12):
            room[i].append([j])
            
    for x in room:
        print(x)

MovieTheater()