import math
is_program_end = False
while is_program_end == False:
    radiuse = float(input("원기둥의 부피를 구하는 프로그램입니다.\n원기둥의 반지름을 입력해주십시오. : "))
    height = float(input("원기둥의 높이를 입력해주십시오. : "))
    print("원기둥의 부피는 " + str(math.pi*radiuse**2*height) + "입니다.")
    is_prompt_end = False
    while is_prompt_end == False:
        user_input = input("다른 원기둥의 부피도 계산해보시겠습니까? (Y / N)")
        if user_input == "N":
            is_program_end = True
            is_prompt_end = True
        elif user_input == "Y":
            is_program_end = False
            is_prompt_end = True
        else:
            print("입력 오류입니다. 다시 입력해주세요.")