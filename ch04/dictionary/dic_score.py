
student = [
    {"kor": 80, "eng": 90, "math": 90},
    {"kor": 60, "eng": 55, "math": 70},
    {"kor": 50, "eng": 60, "math": 73},
]

# 개인별 총점과 평균
print("총점   평균")
for s in student:
    total = s['kor'] + s['math'] + s['eng']
    avg = total / 3
    print("%d  %.2f" % (total, avg))

#과목별 총점과 평균
sum_kor = 0
sum_eng = 0
sum_math = 0

sum_subject = [0, 0, 0]
avg_subject = [0.0, 0.0]

for s in student:
    sum_subject[0] += s['kor']
    sum_subject[1] += s['eng']
    #sum_subject[2] += s['math']

avg_subject[0] = sum_subject[0] / 3
avg_subject[1] = sum_subject[1] / 3

print("국어 합계 : %d점" % sum_subject[0])
print("국어 평균 : %.1f점" % avg_subject[0])
print("수학 합계 : %d점" % sum_subject[1])
print("수학 평균 : %.1f점" % avg_subject[1])