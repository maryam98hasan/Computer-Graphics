import turtle
m = turtle.Turtle()
m.speed(0)
turtle.bgcolor("black")
color=['red','green','blue','pink']
for i in range(360):
    m.pencolor(color[i%4])
    m.width(i/100+1)
    m.forward(i)
    m.left(59)
turtle.done()