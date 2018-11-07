import turtle
import time
def make_square(times):
    times_counter = 0
    while times != times_counter:
        loop_counter = 0
        while 4 != loop_counter:
            if loop_counter < 4:
                t.forward(side)
            if loop_counter < 3:
                t.left(angle)
            loop_counter = loop_counter + 1
        times_counter = times_counter + 1
t = turtle.Turtle()
t.shape("turtle")
side = 100
angle = 90
make_square(5)
time.sleep(3)