# 도형의 면적
width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))

triangleArea = width * height / 2
squareArea = width * height

print('-'*25)
print('삼각형의 넓이 : %.2f' % triangleArea)
print('사각형의 넓이 : %.2f' % squareArea)


