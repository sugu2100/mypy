# 최고 점수
score = [70, 80, 90, 20]
max_idx = 0
for i in range(1, len(score)):
    if score[max_idx] < score[i]:
        max_idx = i

max_v = 0
for i in score:
    if max_v < i:
        max_v = i

print(max_v, max_idx)


#오름 차순 정렬
n = len(score)
for i in range(0, n):
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]

print(score)
