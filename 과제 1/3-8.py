is_program_end = False
is_prompt_end = False
while is_program_end == False:
    is_prompt_end = False
    while is_prompt_end == False:
        weight = float(input("움직이는 물체의 운동에너지를 계산하는 프로그램 입니다.\n킬로그램 단위로 물체의 무게를 입력하세요. : "))
        speed = float(input("미터/초 단위로 물체의 속도를 입력하새요. : "))
        if type(weight and speed) == float:
            is_prompt_end = True
            energe_of_moving_thing = 1 / 2 * weight * speed ** 2
        else:
            print("입력 오류입니다. 다시 입력해주세요.")
    print("움직이는 물체의 에너지는 " + str(energe_of_moving_thing) + "줄 입니다.\n")
    is_prompt_end = False
    while is_prompt_end == False:
        user_input = input("다른 움직이는 물체의 운동에너지도 계산해보시겠습니까? (Y / N)")
        if user_input == "N":
            is_program_end = True
            is_prompt_end = True
        elif user_input == "Y":
            is_program_end = False
            is_prompt_end = True
        else:
            print("입력 오류입니다. 다시 입력해주세요.")