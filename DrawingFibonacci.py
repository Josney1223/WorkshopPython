import turtle
import random

pen = turtle.Turtle()
turtle.colormode(255)
pen.speed(10)

def RandomColor():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)
    
def BaseSquare(d):
    pen.fillcolor(RandomColor())
    pen.begin_fill()
    pen.pendown()
    for i in range(4):
        pen.forward(d)
        pen.left(90)
    pen.end_fill()
    pen.forward(d)

def Fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fib(n-2) + Fib(n-1)

def Drawing(n):
    for i in range(n):
        BaseSquare(Fib(i))
    
Drawing(10)
