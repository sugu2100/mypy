'''
x = input("몇 번 반복할까요? ")
n = int(x)

i = 0
while i < n:
    i += 1
    print(str(i) + "회 반복")

print("합계 : " + str(sum))

# 두 수를 곱하는 프로그램
x = input("첫째 수 : ")
n1 = int(x)
y = input("둘째 수 : ")
n2 = int(y)

print(n1 * n2)

i = 0
while i < 10:
    i += 1
    print("Hello~ ")

i = 0
sum = 0
while i < 10:
    i += 1
    sum += i
    print("i =", i, ", sum = ", sum)

print(sum)


i = 0
while True:
    i += 1
    if i > 10:
        break
    print(i)

for i in range(0, 5):
    for j in range(1, 6):
        n = i*5+j
        print("좌석" + str(n), end=" ")
    print()
'''

x = input("입장객 수 : ")
customer = int(x)
y = input("열 수 : ")
col_num = int(y)

if customer % col_num == 0:
    row_num = int(customer / col_num)
else:
    row_num = int(customer / col_num) + 1
    #row_num = customer // col_num + 1
    
for i in range(0, row_num):
    for j in range(1, col_num + 1):
        seat_num = i * (col_num) + j  #좌석 번호
        if seat_num > customer:
            break
        print("좌석" + str(seat_num), end=" ")
    print()

    

    
    
















    

