# 1 ~ 10 출력
for i in range(1, 11, 1):
    print(i)
print()

# 1 ~ 10 홀수
for i in range(1, 11, 2):
    print(i, end = ' ')
print()
    
for i in range(1, 11):
    if i % 2 != 0:
        print(i, end = ' ')
print()

# 1 ~ 10 합계
sum = 0
for i in range(1, 11):
    sum += i

print("합계 :", sum)
