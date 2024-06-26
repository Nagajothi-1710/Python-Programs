import turtle
import random

scr=turtle.Screen()
scr.title("Space Game by Nagajothi")
scr.bgpic("space_invaders_background.gif")
scr.setup(800,800)
scr.tracer(0)

scr.register_shape("player.gif")
scr.register_shape("invader.gif")

player=turtle.Turtle()
player.shape("player.gif")
player.penup()
player.goto(0,-270)
player.pendown()

enemies=[]
enemyspeed=0.1
for i in range(5):
    enemy=turtle.Turtle()
    enemy.shape("invader.gif")
    x=random.randint(-270,270)
    y=random.randint(150,270)
    enemy.penup()
    enemy.goto(x,y)
    enemies.append(enemy)
bulletspeed=0.2
bulletstate="ready"

bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.goto(0,-260)
bullet.shapesize(0.5)
bullet.setheading(90)

pen=turtle.Turtle()
pen.shape("turtle")
pen.color("yellow")
pen.penup()
pen.goto(0,350)
pen.pendown()
pen.write("Score : 0",align="center",font=("arial",22,"bold"))
pen.hideturtle()

def player_left():
    x=player.xcor()
    x-=20
    if x<=-270:
        x=-270
    player.setx(x)
def player_right():
    x=player.xcor()
    x+=20
    if x>=270:
        x=270
    player.setx(x)
def bullet_fire():
    global bulletstate
    if bulletstate=="ready":
        x=player.xcor()
        y=player.ycor()+10
        bullet.goto(x,y)
        bulletstate="fire"
        bullet.showturtle()
        
scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right,"Right")
scr.onkeypress(bullet_fire,"space")

while True:
    scr.update()

    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    if bullet.ycor()>270:
        bullet.hideturtle()
        bulletstate="ready"
        
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        for e in enemies:
            if x>=270:
                y=e.ycor()
                y-=40
                e.sety(y)
                enemyspeed*=-1
            if x<=-270:
                y=e.ycor()
                y-=40
                e.sety(y)
                enemyspeed*=-1
 
        
        
        
            





