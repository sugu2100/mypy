# 2차원 리스트
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(a)
print("리스트의 크기(행) : ", len(a))
print("리스트의 크기(열) : ", len(a[0]))

for x, y in a:
    print(x, y)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# 리스트 추가
a.append([70, 80])
print(a)

# 합과 평균
sum_v = 0
avg = 0.0
count = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum_v += a[i][j]
        count += 1
    print()

avg = sum_v / count
print("합계 : %d" % sum_v)
print("평균 : %.2f" % avg)
