import turtle
import time

turtle = turtle.Turtle()
turtle.speed(1)
turtle.color("red")
turtle.fillcolor("blue")

## Wait
def Wait(k):
    print(k)
    k = input("Pressione enter para continuar")
    
## Quadrado
def Square():
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    x = 5
    
## Circle
def Circle():
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    
## Hexágono
def Hex():
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(50)
        turtle.left(60)
    turtle.end_fill()

## Octógono
def Octo():
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(50)
        turtle.left(45)
    turtle.end_fill()

## Star
def Star():
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(150)
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(150)
    for i in range(3):
        turtle.forward(50)
        turtle.left(150)
    

while True:
    Star()


