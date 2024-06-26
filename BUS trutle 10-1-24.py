import turtle

scr=turtle.Screen()
    scr.title("School bus")
scr.bgcolor("green")
scr.setup(900,600)

#Rectengle
pen=turtle.Turtle()
pen.shape("turtle")
pen.color("Yellow")
pen.pensize(10)
pen.penup()
pen.goto(-200,-100)
pen.pendown()


pen.fillcolor("yellow")
pen.begin_fill()
pen.forward(400)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(200)
pen.end_fill()
pen.hideturtle()

#Circle
wheel1=turtle.Turtle()
wheel1.shape("turtle")
wheel1.color("black")
wheel1.pensize(10)
wheel1.penup()
wheel1.goto(-100,-130)
wheel1.pendown()
wheel1.fillcolor("black")
wheel1.begin_fill()
wheel1.circle(30)
wheel1.end_fill()
wheel1.hideturtle()

wheel2=turtle.Turtle()
wheel2.shape("turtle")
wheel2.color("black")
wheel2.pensize(10)
wheel2.penup()
wheel2.goto(100,-130)
wheel2.pendown()
wheel2.fillcolor("black")
wheel2.begin_fill()
wheel2.circle(30)
wheel2.end_fill()
wheel2.hideturtle()

#Square
window=turtle.Turtle()
window.shape("turtle")
window.color("light blue")
window.pensize(10)
window.penup()
window.goto(100,10)
window.pendown()

window.fillcolor("light blue")
window.begin_fill()
window.forward(75)
window.left(90)
window.forward(75)
window.left(90)
window.forward(75)
window.left(90)
window.forward(75)
window.left(90)
window.end_fill()
window.hideturtle()


name=turtle.Turtle()
name.color("blue")
name.write("Triveni School",align="center",font=("arial",20,"bold"))
name.hideturtle()




