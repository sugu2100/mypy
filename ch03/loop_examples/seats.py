# 자리배치도 프로그램

customer_num = int(input("입장객 수 입력 : "))
col_num = int(input("좌석 열의 수 입력: "))

if customer_num % col_num == 0:
    row_num = customer_num / col_num
else:
    row_num = customer_num // col_num + 1
    #row_num = int(customer_num / col_num + 1)
print("줄의 수: ", row_num)


print('자리 배치도')
    
for i in range(0, row_num):
    for j in range(1, col_num+1):
        seat_num = i*col_num+j
        if seat_num > customer_num:
            break
        print(seat_num, end=' ')
        
    print()


