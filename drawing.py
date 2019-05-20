import turtle 
import time

pen = turtle.Turtle()
pen.speed(1)
pen.color("red")
pen.fillcolor("blue")

# Quadrado
def Square():
    pen.begin_fill()
    for i in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()
    x = 5

# Circle
def Circle():
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

# Hexágono
def Hex():
    pen.begin_fill()
    for i in range(6):
        pen.forward(50)
        pen.left(60)
    pen.end_fill()

# Octógono
def Octo():
    pen.begin_fill()
    for i in range(8):
        pen.forward(50)
        pen.left(45)
    pen.end_fill()

# Estrela
def Star():
    pen.begin_fill()
    for i in range(3):
        pen.forward(50)
        pen.left(120)
    pen.penup()
    pen.left(90)
    pen.forward(30)
    pen.right(150)
    pen.pendown()
    for i in range(3):
        pen.forward(50)
        pen.left(120)
    pen.end_fill()

# Estrela Pontuda
def EdgeStar():
    pen.speed(1)
    for i in range(11):
        xFrom = 0
        yFrom = (10-i) * 20
        xTo = i * 20
        yTo = 0
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo, yTo)

    for i in range(11):
        xFrom = (10-i) * 20
        yFrom = 0
        xTo = 0
        yTo = - (i * 20)
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo,yTo)

    for i in range(11):
        xFrom = 0
        yFrom = - (10-i) * 20
        xTo = - (i * 20)
        yTo = 0
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo,yTo)

    for i in range(11):
        xFrom = - (10-i) * 20
        yFrom = 0
        xTo = 0
        yTo = (i * 20)
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo,yTo)

# Batimento Cardíaco
def HeartBeat(lenght):
    xStart = 0
    yStart = 0
    yMaxUp = lenght/4
    yMaxDown = -lenght/4

    pen.speed(1)
    pen.pendown()
    pen.goto(lenght*9/24, 0)

    pen.speed(3)
    pen.goto(lenght*11/24, yMaxUp)
    pen.goto(lenght*13/24, yMaxDown)
    pen.goto(lenght*15/24, 0)

    pen.speed(1)
    pen.goto(lenght, 0)
    pen.penup()

    pen.speed(10)
    pen.goto(xStart, yStart)
    pen.clear()

# Desenhar Relógio
def Clock(hora, minutos, radius):
    pen.speed(10)
    xStart = 0
    yStart = 0
    pen.penup()
    
    # Circulo
    pen.right(90)
    pen.forward(radius + radius/10)
    pen.pendown()
    pen.left(90)
    pen.circle(radius + radius/10)
    pen.penup()
    pen.goto(xStart, yStart)

    # Pontos das horas
    for i in range(12):
        pen.forward(radius)
        pen.pendown()
        pen.forward(radius/15)
        pen.stamp()
        pen.penup()
        pen.goto(xStart, yStart)
        pen.left(30)
    
    # Desenhar as horas
    pen.left(90)
    pen.right(30*hora)
    pen.pendown()
    pen.forward(radius/2)
    pen.stamp()
    pen.penup()
    pen.goto(xStart, yStart)
    pen.left(30*hora)
    pen.right(minutos*6)
    pen.pendown()
    pen.forward(radius*3/4)
    pen.penup()
    pen.goto(xStart, yStart)

# Cinema
def MovieTheater(lenght):
    # Desenhar Cadeira
    def DrawChair():
        pen.color("green")
        pen.begin_fill()
        for i in range(4):
            pen.pendown()
            pen.forward(lenght/20)
            pen.left(90)
        pen.end_fill()


    # Criar Array Cadeiras
    room = []
    for i in range(12):
        room.append([i])
        for j in range(19):
            room[i].append([lenght*j/19])
    
    # Desenhar as cadeiras
    for i in range(12):
        pen.speed(100)
        pen.penup()
        pen.goto(- lenght, i*lenght/12)
        pen.pendown()
        for j in range(19):
            pen.penup()
            pen.forward(lenght/19+10)
            pen.pendown()
            DrawChair()

# Jogo da Velha
def CrossGame():

    def BtnClick(x, y):
        print(x,y)

    turtle.bgcolor = ('black')
    turtle._Screen.screensize(600,600)
    lenght = 600

    # Fazer as linhas principais
    for i in range(1,3):
        pen.penup()
        pen.goto(0,i*lenght/3)
        pen.pendown()
        pen.forward(lenght)

    turtle._Screen._onscreenclick(BtnClick, 1)
    turtle._Screen._listen()

    turtle.done()



CrossGame()