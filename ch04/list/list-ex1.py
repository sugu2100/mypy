scores = [90, 45, 67, 59, 85]

index = 0
for score in scores:
    index += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." % index)
        #print("합격")
    else:
        print("%d번 학생은 불합격입니다." % index)
        #print("불합격")
