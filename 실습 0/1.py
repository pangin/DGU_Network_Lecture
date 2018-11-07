import turtle
import random
import time

t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()
s.bgcolor("skyblue")

def draw_snowman(x, y):
    t.penup()
    t.goto(x, y)
    draw_circle(30)
    y = y + -20
    t.goto(x, y)
    draw_circle(20)
    y = y + -60
    t.goto(x, y)
    draw_circle(40)

def draw_circle(size):
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(size)
    t.end_fill()
    t.penup()

while True:
    random.seed(time.time())
    draw_snowman(random.randrange(-100, 100), random.randrange(-100, 100))