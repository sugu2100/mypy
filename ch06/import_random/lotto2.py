
import random

lotto = []
print(len(lotto))
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

'''
for i in range(6):
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
'''

print(lotto)