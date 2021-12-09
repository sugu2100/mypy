# 변수값 교환
blue = 1
red = 2
print("교환전: ")
print("blue =", blue, ", red =", red)

#교환 처리
'''
yellow = blue
blue = red
red = yellow
'''
# 파이썬은 직접 교환함
blue, red = red, blue

print("교환후: ")
print("blue =", blue, ", red =", red)


