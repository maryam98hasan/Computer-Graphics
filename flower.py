import turtle
""" Draw a flower in Pyhton"""

def draw_square(square):
 for i in range(0,2):
     square.forward(120)
     square.right(30)
     square.forward(120)
     square.right(150)
     square.speed(0)
def draw_flower():
 window = turtle.Screen()
 window.bgcolor("pink")

 pen = turtle.Turtle()
 pen.shape("triangle")
 pen.color("#99FF00")

 for i in range(0,10):
     draw_square(pen)
     pen.right(35)
     pen.hideturtle()
 window.exitonclick()

draw_flower()
turtle.done()