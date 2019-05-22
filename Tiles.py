import turtle

pen = turtle.Turtle()

def Size(lenght, high):
    pen.speed(100)
    pen.penup()
    
    def Prime(x):
        y = 1
        divisores = 0
        while(y <= x):
            if (x % y == 0):
                divisores += 1
                y += 1
            else:
                y += 1
        if (divisores == 2):
            return True
        else:
            return False
        
    def Square():
        pen.pendown()
        for i in range(4):
            pen.forward(50)
            pen.left(90)
            
    def DrawTileA(x, y):
        pen.goto(x,y)
        Square()
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
        Square()
        pen.goto(x, y+25)
        pen.goto(x+25, y)
        pen.penup()
        pen.goto(x+25, y+50)
        pen.pendown()
        pen.goto(x+50, y+25)
        pen.penup()
        pen.goto(x,y)
    
    i = 0
    for y in range(high):
        for x in range(lenght):
            if Prime(i):
                DrawTileA(50*x,50*y)
            else:
                DrawTileB(50*x,50*y)
            i += 1
    
    pen.hideturtle()
    turtle.listen()        
    turtle.done()
    
Size(9,9)

