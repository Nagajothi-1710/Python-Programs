import turtle
import random
import math

score=0
scr=turtle.Screen()
scr.title("Space Game Five Turtle")
scr.bgcolor("black")
scr.setup(800,800)
scr.tracer(0)

#register Shapes
player_vertices=((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
scr.register_shape("player",player_vertices)

enemy_vertices=((0,10),(5,7),(3,3),(10,0),(7,4),(8,-6),(0,-10),(-5,-5),(-7,-7),(-10,0),(-5,4),(-1,8))
scr.register_shape("enemy",enemy_vertices)

#player
player=turtle.Turtle()
player.shape("player")
player.color("white")
player.penup()
player.goto(0,0)
player.pendown()
    
#score board
scbo=turtle.Turtle()
scbo.shape("turtle")
scbo.color("yellow")
scbo.penup()
scbo.goto(0,350)
scbo.write("score: 0",align="center",font=("arial",22,"bold"))
scbo.hideturtle()

#bullet
bullets=[]
for i in range(5):
    bullet=turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("red")
    bullet.penup()
    bullet.goto(0,0)
    bullet.shapesize(0.5)
    bullet.state="ready"
    bullet.speed=0.5
    bullets.append(bullet)

def get_heading_to(t1,t2):
    x1=t1.xcor()
    y1=t1.ycor()

    x2=t2.xcor()
    y2=t2.ycor()

    heading=math.atan2(y1-y2,x1-x2)
    heading=heading*180.0/3.14159
    return heading

#enemy
enemies=[]
for i in range(5):
    enemy=turtle.Turtle()
    enemy.shape("enemy")
    enemy.color("brown")
    enemy.penup()
    distance=random.randint(400,600)
    heading=random.randint(0,360)
    enemy.setheading(heading)
    enemy.speed=random.randint(2,5)/100
    enemy.forward(distance)
    enemy.setheading(get_heading_to(player,enemy))
    enemies.append(enemy)
    


#player
def player_right():
    player.right(10)

def player_left():
    player.left(10)


#bullet
def fire_bullet():
    for bullet in bullets:
        if bullet.state=="ready":
            bullet.state="fire"
            bullet.setheading(player.heading())
            bullet.goto(0,0)
            bullet.showturtle()
            break

scr.listen()
scr.onkeypress(player_right,"Right")
scr.onkeypress(player_left,"Left")
scr.onkeypress(fire_bullet,"space")

#main loop
while True:
    scr.update()
    for bullet in bullets:
        if bullet.state=="fire":
            bullet.forward(bullet.speed)
            bullet.showturtle()
        if bullet.xcor()>400 or bullet.xcor()<-400 or bullet.ycor()>400 or bullet.ycor()<-400:
            bullet.hideturtle()
            bullet.state="ready"
            
    for enemy in enemies:
        enemy.forward(enemy.speed)
        for bullet in bullets:
            if enemy.distance(bullet)<20:
                distance=random.randint(400,600)
                heading=random.randint(0,360)
                enemy.setheading(heading)
                enemy.forward(distance)
                enemy.speed+=0.01
                enemy.setheading(get_heading_to(player,enemy))
                bullet.hideturtle()
                bullet.goto(1000,1000)
                bullet.state="ready"
                score+=10
                scbo.clear()
                scbo.write("score:{}".format(score),align="center",font=("arial",22,"bold"))
                
            if enemy.distance(player)<20:
                print("player killed")
                exit()
            
                
        

                                    
        
                
    
