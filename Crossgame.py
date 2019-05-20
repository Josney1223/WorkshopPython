import turtle

player = 0

p1 = False
p2 = False
p3 = False
p4 = False
p5 = False
p6 = False
p7 = False
p8 = False
p9 = False

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
        player += 1
    elif player % 2 == 1 and player < 9:
        DrawCircle(x, y)
        player += 1
    # else:

def OnClickListener(x, y):
    global player, p1, p2, p3, p4, p5, p6, p7, p8, p9    
    
    ## Posição do Click
    # 1 coluna
    if x > 0 and x < 200:
        
        # Posição P1
        if y > 0 and y < 200 and p1 == False:
            p1 = True
            Player(0, 0)
            
        # Posição P2
        elif y > 200 and y < 400 and p2 == False:
            p2 = True
            Player(0, 200)
            
        # Posição P3
        elif y > 400 and p3 == False:
            p3 = True
            Player(0, 400)
 
    # 2 coluna           
    elif x > 200 and x < 400:
        
        # Posição P4
        if y > 0 and y < 200 and p4 == False:
            p4 = True
            Player(200, 0)
        
        # Posição P5
        elif y > 200 and y < 400 and p5 == False:
            p5 = True
            Player(200, 200)
        
        # Posição P6
        elif y > 400 and p6 == False:
            p6 = True
            Player(200, 400)
    
    # 3 coluna
    elif x > 400:
        
        # Posição P7
        if y > 0 and y < 200 and p7 == False:
            p7 = True
            Player(400, 0)
        
        # Posição P8
        elif y > 200 and y < 400 and p8 == False:
            p8 = True
            Player(400, 200)
        
        # Posição P9
        elif y > 400 and p9 == False:
            p9 = True
            Player(400, 400)
            
    # winCondition = WinCondition(spaces)

turtle.bgcolor('black')
turtle.screensize(600, 600)
turtle.setworldcoordinates(0, 0, 600, 600)
turtle.tracer(1, 10)
pen = turtle.Turtle()
pen.speed(5)
pen.hideturtle()
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

pen.speed(500)
pen.pencolor('#00FF00')
turtle.onscreenclick(OnClickListener, 1)
turtle.listen()
turtle.done()
