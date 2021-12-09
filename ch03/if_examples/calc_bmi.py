"""
체질량 지수 BMI(Body Mass Index)를 계산하는 코드다.
비만도는 몸무게를 키(m)의 제곱으로 나눈 결과이다. m -> cm로 환산
BMI가 20미만이면 저체중, 20~24 사이면 정상, 25~29는 과체중, 30 이상이면 비만이다.
"""

name = input("이름을 입력하세요: ")
height = float(input("키(cm)를 입력하세요: "))
height = height / 100
weight = float(input("몸무게(kg)을 입력하세요: "))

bmi = weight / (height ** 2)
print("%s님의 bmi는 %.1lf 입니다." % (name, bmi))

if bmi < 20:
    print("저체중입니다.")
elif bmi < 25:
    print("정상입니다.")
elif bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")

'''
name = input('이름 입력 : ')
w = input('체중 입력: ')
h = input('신장 입력: ')

if w.isnumeric():
    w = int(w)

if h.isnumeric():
    h = int(h) / 100

print('체중 : {}kg'.format(w))
print('신장 : {}m'.format(h))

bmi = w / (h * h)
print('%s님의 BMI : %f' % (name, bmi))
'''



