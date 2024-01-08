import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
list_of_colors = [(199, 12, 32), (158, 63, 20), (249, 236, 25), (209, 88, 225), (40, 77, 187), (239, 229, 4), (38, 217, 69), (227, 160, 50)]
# Create turtle
t = Turtle()

# move turtle position
t.penup()
t.speed(20)
t.setposition(-200, -200)
t.hideturtle()

# Total number of dots
dots_number = 100
for count in range(1, dots_number+ 1):
    t.dot(15, random.choice(list_of_colors))
    t.penup()
    t.forward(50)

    # Number of dots in a row
    if count % 10 == 0:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.right(180)

# Show Screen
screen = Screen()
screen.exitonclick()
