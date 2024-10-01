import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r= random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r, g, b)

def draw_spirograh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed(0)
        tim.pensize(5)
        tim.color(random_color())
        tim.circle(400)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograh(5)

screen = t.Screen()
screen.exitonclick()