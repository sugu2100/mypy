#매개변수가 2개인 람다 함수

# 사칙연산
add = lambda x, y : x + y
print(add(3, 4))
print((lambda x, y : x + y)(3, 4))

sub = lambda x, y : x - y
print(sub(3, 4))
print((lambda x, y : x - y)(3, 4))

mul = lambda x, y : x * y
print(mul(3, 4))
print((lambda x, y : x * y)(3, 4))

div = lambda x, y : x / y
print(div(3, 4))
print((lambda x, y : x / y)(3, 4))




