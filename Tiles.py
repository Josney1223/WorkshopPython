import turtle
import math

pen = turtle.Turtle()

def Size(lenght, high):
    pen.speed(100)
    pen.penup()
    
    def Prime(x):
        divisores = 0
        for y in range(1, x+1):
            if (x % y == 0):
                divisores += 1
        if (divisores == 2):
            return True
        else:
            return False
        
    def BaseSquare():
        pen.pendown()
        for i in range(4):
            pen.forward(50)
            pen.left(90)
   
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
    
    # def Diamond(x, y, d):
    #     pen.penup()
    #     pen.goto(x+25, y + 5*d)
    #     pen.pendown()
    #     if d == 0:
    #         return 0
    #     else:
    #         pen.left(45)
    #         for i in range(4):
    #             p
    #             pen.left(90)
    #         pen.right(45)
    #         return Diamond(x,y,d-1)
        
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
    
    def DrawTileC(x, y):
        pen.goto(x,y)
        BaseSquare()
        SmallerSquare(x, y, 4)
        pen.penup()
         
    
    # def DrawTileD(x, y):
    #     pen.goto(x,y)
    #     BaseSquare()
    #     Diamond(x, y, 4)
            
    i = 1
    for y in range(high):
        for x in range(lenght):
            if Prime(i):
                DrawTileC(50*x,50*y)
            else:
                DrawTileC(50*x,50*y)
            i += 1
    
    pen.hideturtle()
    turtle.listen()        
    turtle.done()
    
Size(5,5)