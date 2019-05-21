import os
import time
import turtle

pen = turtle.Turtle()
turtle.setworldcoordinates(0,0, 800, 500)
pen.speed(5)

def FibonacciClock(hora, minutos):
    def Rect(x, y, lenght, high, fillcolor):
        pen.fillcolor(fillcolor)
        pen.penup()
        pen.goto(x, y)
        pen.begin_fill()
        for i in range(2):
            pen.forward(lenght)
            pen.left(90)
            pen.forward(high)
            pen.left(90)
        pen.end_fill()
        
    while True:
        RealH = hora
        RealM = minutos
        pontos = [5, 3, 2, 1, 1]
        pA = []
        pVM = []
        pV = []
        A1 = False
        A2 = False
        A3 = False
        A4 = False
        A5 = False
        A1C = 'white'
        A2C = 'white'
        A3C = 'white'
        A4C = 'white'
        A5C = 'white'
        Azul = 0
        Vermelho = 0
        Verde = 0

        if hora >= (minutos/5):
            hora -= minutos/5
            Azul = minutos/5
            minutos = 0
        else:
            minutos -= hora*5
            Azul = hora
            hora = 0

        if hora > 0:
            Vermelho = hora
            Verde = 0
        elif minutos > 0:
            Verde = minutos/5
            Vermelho = 0

        for x in pontos:
            if Azul >= x:
                pA.append(x)
                Azul -= x
            elif Vermelho >= x:
                pVM.append(x)
                Vermelho -= x
            elif Verde >= x:
                pV.append(x)
                Verde -= x

        for k in pA:
            if k == 5 and A1 == False:
                A1 = True
                A1C = 'blue'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = 'blue'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = 'blue'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = 'blue'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = 'blue'

        for k in pVM:
            if k == 5 and A1 == False:
                A1 = True
                A1C = 'red'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = 'red'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = 'red'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = 'red'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = 'red'

        for k in pV:
            if k == 5 and A1 == False:
                A1 = True
                A1C = 'green'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = 'green'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = 'green'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = 'green'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = 'green'
                
        pen.speed(10)
        
        ## Color Grid
        Rect(0, 0, 400, 500, A1C)   
        Rect(400, 250, 400, 250, A2C)
        Rect(400, 0, 200, 250, A3C)
        Rect(600, 112, 200, 113, A4C)
        Rect(600, 0, 200, 113, A5C)

        ## Make Grid
        pen.width(50)
        pen.goto(0,0)
        pen.pendown()
        for i in range(2):
            pen.forward(800)
            pen.left(90)
            pen.forward(500)
            pen.left(90)

        pen.width(25)
        pen.goto(400,0)
        pen.pendown()
        pen.goto(400,500)
        pen.goto(400,250)
        pen.goto(800,250)
        pen.goto(600,250)
        pen.goto(600,0)
        pen.goto(600,113)
        pen.goto(800,113)
        
        
        for i in range (5):
            for y in range(60):
                time.sleep(1)
        
        RealM += 5
        if RealM == 60:
            RealM = 0
            RealH += 1
        hora = RealH
        minutos = RealM

FibonacciClock(10, 35)
