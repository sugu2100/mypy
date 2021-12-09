# 재귀 함수로 계산하기
# factorial : n! = (nx(n-1)x(n-2)x...x3x2x1)
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(1)) # 1
print(facto(2)) # 2 * facto(1)
print(facto(3)) # 3 * facto(2)
print(facto(10)) # 4 * facto(3)

