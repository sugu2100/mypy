# 전역변수의 유효 범위 - global 키워드 사용
def one_up():
    global x
    x += 1
    return x

x = 1
print(one_up())
print(one_up())
print(one_up())
# x값 출력
print(x)
