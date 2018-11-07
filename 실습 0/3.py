import turtle

t = turtle.Turtle()
t.shape("turtle")

def calc_graph(x):
    result = (x ** 2) + 1
    return result

def init_graph():
    t.pendown()
    t.goto(400, 0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(0, 400)
    t.penup()
    t.goto(0, 0)

def draw_graph(x, y):
    t.pendown()
    t.goto(x, y)

x_pos = 0
y_pos = 0
init_graph()
while x_pos != 150:
    y_result = calc_graph(x_pos)
    draw_graph(x_pos, y_result * 0.01)
    x_pos = x_pos + 1
    y_pos = y_pos + 1