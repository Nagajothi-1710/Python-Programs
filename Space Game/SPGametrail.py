import turtle
import random

score=0

scr=turtle.Screen()
scr.title("Space game crated by Nagajothi")
scr.bgpic("space_invaders_background.gif")
scr.setup(800,800)
scr.register_shape("player.gif")
scr.register_shape("invader.gif")
scr.tracer(0)

#Score board
scbo=turtle.Turtle()
scbo.shape("turtle")
scbo.color("yellow")
scbo.penup()
scbo.goto(0,350)
scbo.pendown()
scbo.write("score: 0",align="center",font=("arial",22,"bold"))
scbo.hideturtle()

#player
player=turtle.Turtle()
player.shape("player.gif")
player.penup()
player.goto(0,-280)
player.pendown()

#bullet
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.left(90)
bullet.shapesize(0.5)
bullet.penup()
bullet.goto(0,-270)
bullet.hideturtle()
bulletstate="ready"
bulletspeed=0.2

#enemie
enemies=[]
enemiespeed=0.02
for i in range(5):
    enemie=turtle.Turtle()
    enemie.shape("invader.gif")
    x=random.randint(-280,280)
    y=random.randint(260,280)
    enemie.penup()
    enemie.goto(x,y)
    enemies.append(enemie)
    
#player
def player_left():
    x=player.xcor()
    x-=20
    if x<-275:
        x=-275
    player.setx(x)
    
def player_right():
    x=player.xcor()
    x+=20
    if x>275:
        x=275
    player.setx(x)

#bullet
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.goto(x,y)
        bullet.showturtle()
           
scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right,"Right")
scr.onkeypress(fire_bullet,"space")

while True:
    scr.update()
#enemie
    for enemie in enemies:
        x=enemie.xcor()
        x+=enemiespeed
        if x<-275:
            enemiespeed*=-1
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
        enemie.setx(x)
        if x>275:
            enemiespeed*=-1
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
        if bullet.distance(enemie)<20:
            bullet.hideturtle()
            bullet.goto(-500,-500)
            x=random.randint(-280,280)
            y=random.randint(260,280)
            enemie.penup()
            enemie.goto(x,y)
            score+=10
            scbo.clear()
            scbo.write("score: {}".format(score),align="center",font=("arial",22,"bold"))
                       
        if enemie.ycor()<=-275:
            exit()
            
#bullet             
            
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
    
