print("for ~ in() 사용")
scores = [90, 45, 67, 59, 85]
index = 0
for score in scores:
    index = index + 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % index)
    else:
        print("%d번 학생은 불합격입니다." % index)

print("="*40)

print("for ~ range() 사용")
n = len(scores)
for i in range(0, n):
    if scores[i] >= 60:
        print("%d번 학생은 합격입니다." % (i+1))
    else:
        print("%d번 학생은 불합격입니다." % (i+1))
