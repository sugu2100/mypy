# 1부터 10까지 합계

sum = 0
sum = sum + 1;
sum = sum + 2;
sum = sum + 3;
sum = sum + 4;
sum = sum + 5;

print(sum)

i = 1
sum = 0
while i < 11:
    sum += i
    print("i = ", i, "sum = ", sum)
    i += 1

print("합계는", sum)

