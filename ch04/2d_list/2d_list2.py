
a = [
      [10, 21],
      [30, 40],
      [50, 60]
    ]

print("리스트의 크기(행) : ", len(a))
print("리스트의 크기(열) : ", len(a[0]))
print("리스트의 크기(열) : ", len(a[1]))

# 리스트 내의 값 출력 - range() 사용
for i in range(len(a)):  #0~3
    for j in range(len(a[i])): #0~2
        print(a[i][j], end=' ')
    print()
print()

# 리스트 추가
a.append([70, 80])
print(a)

# 리스트 내의 값 출력
for x, y in a:
    print(x, y)

# 연산
total = 0
avg = 0.0
count = 0  # 2차원 리스트는 개수를 세야함
for i in range(len(a)):  #0~3
    for j in range(len(a[i])): #0~2
        total += a[i][j]
        count += 1
    print()
    
avg = total / count # 평균 = 합계 / 개수
print("합계 : %d" % total)
print("평균 : %.2f" % avg)















    
