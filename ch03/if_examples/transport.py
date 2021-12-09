# 교통
money = 3000
card = False
if money >= 4000 or card:
    print("택시를 탄다")
elif money >= 2000 or not card:
    print("버스를 탄다")
else:
    print("걸어간다")

print('='*30)

pocket = ['paper', '스마트폰', 'money']
if 'coin' in pocket:
    print('택시를 탄다')
else:
    print('지하철을 탄다')
