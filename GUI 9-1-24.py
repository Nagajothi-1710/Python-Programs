import turtle

scr=turtle.Screen()
scr.title("My first screen")
scr.bgcolor("green")
scr.setup(1000,900)#width, height

pen=turtle.Turtle()
pen.shape("turtle")
pen.color("yellow")
pen.pensize(10)
pen.circle(100)
#Square
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)

