import turtle
import math

pen = turtle.Turtle()

def Size(lenght, high, k):
    pen.speed(100)
    pen.penup()

    ## Checks e Polígonos regulares
    # Check se é Primo
    def Prime(x):
        divisores = 0
        for y in range(1, x+1):
            if (x % y == 0):
                divisores += 1
        if (divisores == 2):
            return True
        else:
            return False

    # Desenhar Quadrado Base    
    def BaseSquare():
        pen.pendown()
        for i in range(4):
            pen.forward(50)
            pen.left(90)

    # Desenhar Hexágono
    def BaseHex():
        pen.pendown()
        pen.left(90)
        for i in range(6):
            pen.forward(50)
            pen.right(60)
        pen.right(90)
        pen.pendown()
    
    # Desenhar quadrados pequenos dentro do quadrado   
    def SmallerSquare(x, y, d):
        pen.penup()
        pen.goto(x+d*5,y+d*5)
        pen.pendown()
        if d == 0:
            return 0
        else:
            for i in range(4):
                pen.forward(50-d*10)
                pen.left(90) 
            return SmallerSquare(x,y,d-1) 

    ## Lajotas
    # Lajota Diagonal Esq-Dir
    def DrawTileA(x, y):
        pen.goto(x,y)
        BaseSquare()
        pen.goto(x, y+25)
        pen.goto(x+25, y+50)
        pen.penup()
        pen.goto(x+50, y+25)
        pen.pendown()
        pen.goto(x+25, y)
        pen.penup()
        pen.goto(x,y)

    # Lajota Diagonal Dir-Esq    
    def DrawTileB(x, y):
        pen.goto(x,y)
        BaseSquare()
        pen.goto(x, y+25)
        pen.goto(x+25, y)
        pen.penup()
        pen.goto(x+25, y+50)
        pen.pendown()
        pen.goto(x+50, y+25)
        pen.penup()
        pen.goto(x,y)

    # Quadrado com quadradinhos dentro
    def DrawTileC(x, y):
        pen.goto(x,y)
        BaseSquare()
        SmallerSquare(x, y, 6)
        pen.penup()

    # Hexágono
    def DrawTileD(x, y, high):
        pen.penup()
        if high % 2 == 0:
            pen.goto(43+x, y)
        else:
            pen.goto(x, y)
        BaseHex()
        
    ## Definições    
    i = 1
    # Cálculo D
    # se Hexágono d = 87
    # se quadrado d = 50
    # Definido por Primos k = 1
    if k == 1:
        for y in range(high):
            for x in range(lenght):
                if Prime(i):
                    DrawTileD(87*x,76*y, y+1)
                else:
                    DrawTileD(87*x,76*y, y+1)
                i += 1
                
    # Definido por Pares k = 2
    elif k == 2:        
        for y in range(high):
            for x in range(lenght):
                if i % 2 == 0:
                    DrawTileA(50*x,50*y)
                else:
                    DrawTileB(50*x,50*y)
                i += 1
    
    pen.hideturtle()
    turtle.listen()        
    turtle.done()
    
Size(5,5, 1)
