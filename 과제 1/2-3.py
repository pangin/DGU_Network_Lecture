import math
is_program_end = False
while is_program_end == False:
    radius = float(input("반지름으로 원의 넓이를 구하는 프로그램입니다.\n원의 반지름을 입력해주세요. : "))
    print("반지름이 " + str(radius) + "인 원의 넓이는 " + str(math.pi * radius * 2) + "입니다.")
    is_prompt_end = False
    while is_prompt_end == False:
        user_input = input("다른 반지름의 원도 계산해보시겠습니까? (Y / N)")
        if user_input == "N":
            is_program_end = True
            is_prompt_end = True
        elif user_input == "Y":
            is_program_end = False
            is_prompt_end = True
        else:
            print("입력 오류입니다. 다시 입력해주세요.")