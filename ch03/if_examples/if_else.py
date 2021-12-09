#car_speed

speed = int(input('속도 입력: '))
limit_speed = 50   #제한 속도

if speed > 50:
    print("안전 속도 위반 : 과태료 10만원 부과 대상")
else:
    print("안전 속도 준수!!")
