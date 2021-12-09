import random

lotto = []
while len(lotto) < 6:
    print(len(lotto))
    n = random.randint(1, 45)
    print(n)
    if n not in lotto:
        lotto.append(n)

print(lotto)
