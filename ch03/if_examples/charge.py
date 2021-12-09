
print("♣ 놀이 공원 입장료 계산 ♣")

age = 15
charge = 0;
if age < 8:
    print('미취학 아동입니다.')
    charge = 1000
elif age >= 8 and age < 14:
    print('초.중등학생입니다.')
    charge = 2000
elif age >= 14 and age < 20:
    print('초.중등학생입니다.')
    charge = 2500
else:
    print('초.중등학생입니다.')
    charge = 3000

#print("입장료는 " + str(charge) + "원입니다.")
print("입장료는 " + format(charge, ',d') + "원입니다.")
    
