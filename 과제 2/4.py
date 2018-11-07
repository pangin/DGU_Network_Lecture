import turtle
import time

t = turtle.Turtle()
t.shape("turtle")


def draw_line(times):
    for i in range(times):
        t.forward(100)
        t.backward(100)
        t.right(360 / times)


draw_line(12)
time.sleep(5)