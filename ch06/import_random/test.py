import random

# 로또 번호 6개 저장하기(중복 제거)
# 5개 저장 오류
lotto = []

for i in range(6):
    x = random.randint(1, 45)
    if x not in lotto:
        lotto.append(x)

print(lotto)

''''
x = random.randint(1, 45)
lotto.append(x)
print(lotto)
'''



"""
while len(lotto) < 6:
    x = random.randint(1, 45)
    if x not in lotto:
        lotto.append(x)

print(lotto)
"""