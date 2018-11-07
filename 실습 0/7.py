import math

PI = math.pi

def circleArea(radius):
    area = PI * radius ** 2
    print("반지름이 " + str(radius) + "인 원의 넓이: " + str(area))

def circleCircumference(radius):
    circumference = 2 * PI * radius
    print("반지름이 " + str(radius) + "인 원의 둘레: " + str(circumference))

rad = int(input("원의 반지름을 입력해주세요."))
circleArea(rad)
circleCircumference(rad)
