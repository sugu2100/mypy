# 거듭제곱
def mypow(x, y):
    num = 1
    for i in range(0, y):
        num *= x
    return num

n1 = mypow(2, 5)
n2 = pow(2, 5)     #내장 함수
print(n1)
print(n2)
