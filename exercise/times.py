# 3과 5의 배수의 합
# 범위 : 1~100

sum = 0
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print(i)
    #print(i * 3)

print(sum)
