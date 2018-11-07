def add(a, b):
    print("(" + str(a) + " + " + str(b) + ") = " + str(a + b))


def div(a, b):
    print("(" + str(a) + " / " + str(b) + ") = " + str(a / b))


def sub(a, b):
    print("(" + str(a) + " - " + str(b) + ") = " + str(a - b))


def mlt(a, b):
    print("(" + str(a) + " * " + str(b) + ") = " + str(a * b))


select = input("사칙연산자 +, -, *, / 중에서 수행하고 싶으신 연산 하나를 입력해주세요: ")
if select == "+":
    add(float(input("첫번째 수를 입력해주세요: ")), float(input("두번째 수를 입력해주세요: ")))
elif select == "-":
    sub(float(input("첫번째 수를 입력해주세요: ")), float(input("두번째 수를 입력해주세요: ")))
elif select == "*":
    mlt(float(input("첫번째 수를 입력해주세요: ")), float(input("두번째 수를 입력해주세요: ")))
elif select == "/":
    div(float(input("첫번째 수를 입력해주세요: ")), float(input("두번째 수를 입력해주세요: ")))
else:
    print("입력 값이 잘못되었습니다.")