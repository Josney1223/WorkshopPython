import turtle
import time

player = 0
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
        pen.goto(xTo, yTo)

    for i in range(11):
        xFrom = 0
        yFrom = - (10-i) * 20
        xTo = - (i * 20)
        yTo = 0
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo, yTo)

    for i in range(11):
        xFrom = - (10-i) * 20
        yFrom = 0
        xTo = 0
        yTo = (i * 20)
        pen.penup()
        pen.goto(xFrom, yFrom)
        pen.pendown()
        pen.goto(xTo, yTo)

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
    def DrawCross(x, y):
        pen.penup()
        pen.goto(x+20, y + 180)
        pen.pendown()
        pen.goto(x+180, y + 20)
        pen.penup()
        pen.goto(x + 20, y + 20)
        pen.pendown()
        pen.goto(x + 180, y + 180)

    def DrawCircle(x, y):
        pen.penup()
        pen.goto(x + 180, y + 100)
        pen.pendown()
        pen.circle(80)

    def Player(x, y):
        global player

        if player % 2 == 0 and player < 9:
            DrawCross(x, y)
        elif player % 2 == 1 and player < 9:
            DrawCircle(x, y)
        # else:

    def OnClickListener(x, y):
        global player

        # Posição do Click
        if x > 0 and x < 200:
            if y > 0 and y < 200:
                Player(0, 0)
            elif y > 200 and y < 400:
                Player(0, 200)
            elif y > 400:
                Player(0, 400)
        elif x > 200 and x < 400:
            if y > 0 and y < 200:
                Player(200, 0)
            elif y > 200 and y < 400:
                Player(200, 200)
            elif y > 400:
                Player(200, 400)
        elif x > 400:
            if y > 0 and y < 200:
                Player(400, 0)
            elif y > 200 and y < 400:
                Player(400, 200)
            elif y > 400:
                Player(400, 400)
        player += 1
        #winCondition = WinCondition(spaces)

    turtle.bgcolor('black')
    turtle.screensize(600, 600)
    turtle.setworldcoordinates(0, 0, 600, 600)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(10)
    pen.width(3)
    pen.color('white')
    pen.penup()

    # Linhas Horizontais
    for i in range(1, 3):
        pen.penup()
        pen.goto(0, i*200)
        pen.pendown()
        pen.forward(600)

    # Linhas Verticais
    pen.left(90)
    for i in range(1, 3):
        pen.penup()
        pen.goto(i*200, 0)
        pen.pendown()
        pen.forward(600)

    pen.pencolor('#00FF00')
    turtle.onscreenclick(OnClickListener, 1)
    turtle.listen()
    turtle.done()


CrossGame()
