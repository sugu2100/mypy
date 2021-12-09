import random

lotto = []

for i in range(6):
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
'''
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
'''
print(lotto)
