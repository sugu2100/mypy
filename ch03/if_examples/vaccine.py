# 백신 접종 대상자
'''
 - 19세이상 65세 이하이면 출생 년도 끝자리에 따른 접종, 그렇지 않으면 하반기 일정 확인
'''

age = int(input("나이 입력 : "))
if age >= 29 and age <= 65:
    end_num = int(input('출생 년도 끝자리 입력 : '))
    if end_num == 1 or end_num == 6:
        print("월요일 접종")
    elif end_num == 2 or end_num == 7:
        print("화요일 접종")
    elif end_num == 3 or end_num == 8:
        print("수요일 접종")
    elif end_num == 4 or end_num == 9:
        print("목요일 접종")
    elif end_num == 5 or end_num == 0:
        print("금요일 접종")
else:
    print("하반기 일정 확인")