import math
is_program_end = False
while is_program_end == False:
    x = float(input("두 점의 거리를 계산하는 프로그램 입니다.\n첫번째 x점을 입력해주십시오. : "))
    y = float(input("첫번째 y점을 입력해주십시오. : "))
    x_0 = float(input("두번째 x점을 입력해주십시오. : "))
    y_0 = float(input("두번쪠 y점을 입력해주십시오. : "))
    print("두 점 사이의 거리는 " + str(math.sqrt((x - x_0) ** 2 + (y - y_0) ** 2)) + "입니다.")
    is_prompt_end = False
    while is_prompt_end == False:
        user_input = input("다른 두 점의 거리도 계산해보시겠습니까? (Y / N)")
        if user_input == "N":
            is_program_end = True
            is_prompt_end = True
        elif user_input == "Y":
            is_program_end = False
            is_prompt_end = True
        else:
            print("입력 오류입니다. 다시 입력해주세요.")