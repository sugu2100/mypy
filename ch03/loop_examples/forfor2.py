
for i in range(0, 5):
    for j in range(0, i+1):
        print("$", end='')
    print()
print("="*20)

for i in range(0, 5):
    for j in range(0, 5-i):
        print("$", end='')
    print()
print("="*20)

for i in range(0, 5):
    for j in range(1, 6):
        print(i*5+j, end=' ')
    print()
print("="*20)

