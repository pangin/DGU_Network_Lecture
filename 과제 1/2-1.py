import datetime
is_program_end = False
while is_program_end == False:
    is_prompt_end = False
    while is_prompt_end == False:
        name = input("사용자가 100살이 되는 연도를 계산해주는 프로그램 입니다.\n이름을 입력해주세요. : ")
        age = int(input("나이를 입력해주세요. : "))
        if ((type(name) is str) and (type(age) is int)) is True:
            year = datetime.date.today().year
            is_prompt_end = True
        else:
            print("입력오류입니다. 다시 입력해주세요.")
    print(name + "씨는 " + str(year + (100 - age)) + "년에 100살이시네요!")
    is_prompt_end = False
    while is_prompt_end == False:
        user_input = input("다른 사용자도 계산해보시겠습니까? (Y / N)")
        if user_input == "N":
            is_program_end = True
            is_prompt_end = True
        elif user_input == "Y":
            is_program_end = False
            is_prompt_end = True
        else:
            print("입력 오류입니다. 다시 입력해주세요.")