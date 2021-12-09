# 3
x = all([1, 2, abs(-3)-3])
print(x)
y = chr(ord('a'))
print(y)

# 4
def positive(a):
    a2 = []
    for i in a:
        if i > 0:
            a2.append(i)
    return a2

v = [1, -2, 3, -5, 8, -3]
print(positive(v))
# 람다식으로 구현
positive2 = lambda x : x > 0
result = filter(positive2, v)
print(list(result))

# 5
print(hex(234))
print(int('0xea', 16))

# 7
v = [-8, 2, 7, 5, -3, 5, 0, 1]
max_v = max(v)
min_v = min(v)
print(max_v + min_v)

# 8
print(17 / 3)
print(round(17/3, 4))

# 12
import time
now = time.strftime("%Y/%m/%d %H:%M:%S")
print(now)

# 13
import random
lotto = []
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

print(lotto)