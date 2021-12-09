
while True:
    answer = input('반복을 계속 할까요?(y/n)')

    if answer == 'y' or answer == 'Y':
        print('반복을 계속 합니다.')
    elif answer == 'n' or answer == 'N':
        print('반복을 중단 합니다.')
        break
    else:
        print('정상 답변이 아닙니다.')
