# 키오스크에서 사용하는 언어 선택 프로그램

try:
    print('1.한국어\t 2.English')
    select_num = input('언어 선택(Choose your language): ')

    if int(select_num) == 1:
        menu = "1.샌드위치 \t 2.햄버거 \t 3.커피 \t 4.아이스크림"
    elif int(select_num) == 2:
        menu = "1.Sandwich \t 2.Burger \t 3.Coffee \t 4.Icecream"
    else:
        print("1, 2번만 지원합니다.")
    print(menu)
except:
    print("잘못된 입력입니다. 다시 입력해주세요")






















    
    
