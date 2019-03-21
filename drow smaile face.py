import turtle
bob = turtle.Turtle()  # and set bob as our turtle
bob.speed(0)
def points(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
def circles(color, size, angle):
    # Function to create circles and colors them
    bob.fillcolor(color)
    bob.begin_fill()
    if angle == 360:
        bob.circle(size)
    else:
        bob.circle(size, angle)
    bob.end_fill()


# Start Main Code Ending the Functions
points(0, -205)
circles('yellow', 180, 360)

points(-70, 40)
circles('black', 30, 360)

points(70, 40)
circles('black', 30, 360)

bob.right(70)
points(-80, -70)
circles('black', 80, 140)
bob.hideturtle()
turtle.done()