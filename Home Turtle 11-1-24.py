import turtle

scr=turtle.Screen()
scr.title("Home Turtle")
scr.bgcolor("green")
scr.setup(900,600)

#Triangle
pen=turtle.Turtle()
pen.shape("turtle")
pen.color("brown")
pen.pensize(10)

pen.penup()
pen.goto(-100,100)
pen.pendown()

pen.fillcolor("brown")
pen.begin_fill()
for i in range(3):
    pen.forward(200)
    pen.left(120)
pen.end_fill()
pen.hideturtle()

#Square
sq=turtle.Turtle()
sq.shape("turtle")
sq.color("yellow")
sq.pensize(10)

sq.penup()
sq.goto(-105,100)
sq.down

sq.fillcolor("yellow")
sq.begin_fill()
for i in range(4):
    sq.forward(210)
    sq.right(90)
sq.end_fill()
sq.hideturtle()

#rectangle
rec=turtle.Turtle()
rec.shape("turtle")
rec.color("blue")
rec.pensize(5)

rec.penup()
rec.goto(-25,-20)
rec.pendown()

rec.fillcolor("blue")
rec.begin_fill()
for i in range(2):
    rec.forward(50)
    rec.right(90)
    rec.forward(90)
    rec.right(90)
rec.end_fill()
rec.hideturtle()

#square window
sqw=turtle.Turtle()
sqw.shape("turtle")
sqw.color("light blue")
sqw.pensize(5)

sqw.penup()
sqw.goto(50,60)
sqw.pendown()

sqw.fillcolor("light blue")
sqw.begin_fill()
for i in range(4):
    sqw.forward(50)
    sqw.right(90)
sqw.end_fill()
sqw.hideturtle()

#line window1
li=turtle.Turtle()
li.color("black")
li.shape("turtle")
li.pensize(2)

li.penup()
li.goto(48,30)
li.pendown()
li.hideturtle()

li.forward(55)

#line2 window
li2=turtle.Turtle()
li2.color("black")
li2.shape("turtle")
li2.pensize(2)

li2.penup()
li2.goto(75,62)
li2.pendown()

li2.right(90)
li2.forward(55)
li2.hideturtle()








