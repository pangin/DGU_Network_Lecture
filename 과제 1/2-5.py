import turtle
import time
def forward_left(times):
    counter = 0
    while counter != times:
        t.forward(side)
        t.left(120)
        counter = counter + 1
side = 100
t = turtle.Turtle()
t.shape("turtle")
forward_left(3)
time.sleep(5)