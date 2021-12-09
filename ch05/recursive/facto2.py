# 1부터 n까지의 곱 구하기(1x2x3x...xn)
def facto(n):
    gob = 1
    for i in range(1, n+1):
        gob *= i
        #print(i, gob)
    return gob

print(facto(1))
print(facto(4))
print(facto(5))
