import random
from turtle import Turtle, Screen
import turtle as turtle_module

turtle = Turtle()
turtle_module.colormode(255)


def random_color():
    """Returns (r,g,b) tuple :- Generates Ramdom r,g,b Values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


distance = 20
number_of_test_cases = 300

angles_list = [0, 90, 180, 270]
turtle.shape('circle')
turtle.shapesize(0.5)
turtle.pensize(10)
turtle.speed(0)

for _ in range(number_of_test_cases):
    angle = random.choice(angles_list)
    turtle.color(random_color())
    turtle.forward(distance)
    turtle.setheading(angle)



screen = Screen()
screen.exitonclick()
