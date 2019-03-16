import turtle
m=turtle.Turtle()
m.speed(0)
def flower():
    for i in range(13):
        m.left(360/10)
        m.circle(100,60)
        m.left(120)
        m.circle(100,60)
m.hideturtle()
flower()
turtle.done()