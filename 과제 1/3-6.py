import turtle
import time
t = turtle.Turtle()
t.shape("turtle")
is_prompt_end = False
while is_prompt_end == False:
    start_point_x = float(input("거북이를 어디에 둘까요?\n시작 점 x를 입력해주세요."))
    start_point_y = float(input("\n시작 점 y를 입력해주세요."))
    end_point_x = float(input("거북이를 어디로 움직일까요?\n끝 점 x를 입력해주세요."))
    end_point_y = float(input("끝 점 y를 입력해주세요."))
    if type(start_point_x and start_point_y and end_point_x and end_point_y) == float:
        is_prompt_end = True
    else:
        print("정수나 실수를 입력해주십시오")

t.goto(start_point_x, start_point_y)
distance = t.distance(end_point_x, end_point_y)
t.goto(end_point_x, end_point_y)
t.write("직선 길이는 " + str(distance) + "입니다.", False, align = "left")

time.sleep(5)