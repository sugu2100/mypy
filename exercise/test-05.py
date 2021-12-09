# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

"""
cal = UpgradeCalculator()
cal.add(10)
cal.minus(3)

print(cal.value)
"""

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)

print(cal2.value)

# 4번
numbers = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x : x > 0, numbers)))

# 5번
print(hex(234))
print(int('0xea', 16))

# 6번
li = [1, 2, 3, 4]
print(list(map(lambda x : x * 3, li)))

# 7번
li = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(li) + min(li))

# 8번
print(round(17/3, 4))

# 12번
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 13번
import random
lotto = []
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

print(lotto)