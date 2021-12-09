# 점수 리스트 생성
score = [70, 80, 55, 60, 90, 40]

# 최고 점수
max = score[0]
for i in score:
    if max < i:
        max = i

print("최고 점수 : %d" % max)

# 최고 점수의 위치
max_idx = 0
n = len(score)
for i in range(1, n):
    if score[max_idx] < score[i]:
        max_idx = i

print("최고 점수의 위치 : %d" % max_idx)
   




