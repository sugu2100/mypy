# 점수 리스트 생성
A = [70, 60, 55, 75, 95, 90, 80, 70, 85, 100]
total = 0

# 합계, 개수, 평균
for i in A:
    total += i
    print(i)

count = len(A) #len(리스트) - 개수
avg = total / count

print("개수 : %d개" % count)
print("합계 : %d점" % total)
print("합계 : %d점" % sum(A)) # sum(리스트)-합계
print("평균 : %.2f점" % avg)


