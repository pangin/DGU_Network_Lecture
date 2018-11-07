import turtle
import time

t = turtle.Turtle()
t.shape("turtle")

def draw_hexagon(time):
    for i in range(time):
        for i in range(6):
            t.forward(100)
            t.left(60)
        t.forward(100)
        t.right(60)


draw_hexagon(6)
time.sleep(5)