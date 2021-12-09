# 점수 리스트 선언 및 생성
score = [70, 80, 50, 60, 90, 40]
sum_v = 0
for i in score:
    sum_v += i

count = len(score)
avg = sum_v / count

print("개수 :", count)
print("합계 :", sum_v)
print("평균 :", avg)

# 최고 점수
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i

# 최저 점수
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i

print("최고 점수 :", max_v)
print("최저 점수 :", min_v)

#함수 sum, max, min
print("합계 :", sum(score))
print("최고 점수 :", max(score))
print("최고 점수 :", min(score))
