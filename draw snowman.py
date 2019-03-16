#project
import turtle
turtle.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(0)
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
# Below three statements for drawing snowman body
draw_circle("#ffffff", 30, 0, -40)
draw_circle("#ffffff", 40, 0, -100)
draw_circle("#ffffff", 60, 0, -200)

draw_circle("#ffffff", 2, -10, -10)  # Drawing left eye
draw_circle("#ffffff", 2, 10, -10)  # Drawing right eye
draw_circle("#FF6600", 3, 0, -15)  # Drawing nose

# Below three statements for drawing buttons
draw_circle("#ffffff", 2, 0, -35)
draw_circle("#ffffff", 2, 0, -45)
draw_circle("#ffffff", 2, 0, -55)

# Code for drawing left arm
t.penup()
t.goto(-15, -35)
t.pendown()
t.pensize(5)
t.goto(-75, -50)
# Code for drawing right arm
t.penup()
t.goto(15, -35)
t.pendown()
t.pensize(5)
t.goto(75, -50)

# Code for drawing hat
t.penup()
t.goto(-35, 8)
t.color("black")
t.pensize(6)
t.pendown()
t.goto(35, 8)

t.goto(30, 8)
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(15)
t.left(90)
t.forward(60)
t.left(90)
t.forward(15)
t.end_fill()
m=turtle.Turtle()
m.penup()
m.goto(270,-180)
m.pendown()
m.speed(0)
def flower():
    for i in range(13):
        m.begin_fill()
        m.color("pink")
        m.pencolor("black")
        m.left(360/10)
        m.circle(60,60)
        m.left(120)
        m.circle(60,60)
        m.end_fill()
m.pencolor("green")
m.left(90)
m.forward(170)
m1=turtle.Turtle()
m1.penup()
m1.goto(-140,-180)
m1.pendown()
m1.speed(0)
#draw the second flower
def flower2():
    for i in range(13):
        m1.begin_fill()
        m1.color("pink")
        m1.pencolor("black")
        m1.left(360/10)
        m1.circle(60,60)
        m1.left(120)
        m1.circle(60,60)
        m1.end_fill()
m1.pencolor("green")
m1.left(90)
m1.forward(170)
m1.hideturtle()
flower2()
flower()
turtle.done()