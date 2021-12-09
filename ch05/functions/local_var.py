# 지역변수의 유효 범위
def one_up(x):
    x = x + 1
    return x

num = one_up(1)
print("num = %d" % num)
print("x = %d" % x)
