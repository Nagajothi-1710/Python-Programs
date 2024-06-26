import turtle

scr=turtle.Screen()
scr.title("Traffic Signal")
scr.bgcolor("green")
scr.setup(900,600)

#Dimond Shape
pen=turtle.Turtle()
pen.color("yellow")
pen.shape("turtle")
pen.pensize(10)
pen.left(45)
pen.penup()
pen.goto(0,-125)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
for i in range (4):
    pen.forward(250)
    pen.left(90)
pen.end_fill()
pen.hideturtle()

#rectangle
rec=turtle.Turtle()
rec.shape("turtle")
rec.color("black")
rec.pensize(5)
rec.penup()
rec.goto(-50,-60)
rec.pendown()
rec.fillcolor("black")
rec.begin_fill()
for i in range(2):
    rec.forward(100)
    rec.left(90)
    rec.forward(230)
    rec.left(90)
rec.end_fill()
rec.hideturtle()

#circle1
cir=turtle.Turtle()
cir.shape("turtle")
cir.color("green")
cir.pensize(5)
cir.penup()
cir.goto(-3,100)
cir.pendown()
cir.fillcolor("green")
cir.begin_fill()
cir.circle(25)
cir.end_fill()
cir.hideturtle()

#circle2
cir2=turtle.Turtle()
cir2.shape("turtle")
cir2.color("yellow")
cir2.pensize(5)
cir2.penup()
cir2.goto(-3,30)
cir2.pendown()
cir2.fillcolor("yellow")
cir2.begin_fill()
cir2.circle(25)
cir2.end_fill()
cir2.hideturtle()

#circle3
cir3=turtle.Turtle()
cir3.shape("turtle")
cir3.color("red")
cir3.pensize(5)
cir3.penup()
cir3.goto(-3,-40)
cir3.pendown()
cir2.fillcolor("red")
cir3.begin_fill()
cir3.circle(25)
cir3.end_fill()
cir3.hideturtle()




    








