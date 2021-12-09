# 성적 처리를 위해 이차원 리스트로 만든다.

with open('scorelist.txt', 'r') as f:
    li = []
    for i in range(4):
        li.append(f.readline().split()) #한줄씩 공백으로 분리 저장
    print(li)

    for i in range(4):
        li[i][1] = int(li[i][1])  #계산을 위해 정수형 변환
        li[i][2] = int(li[i][2])
        li[i].append(li[i][1] + li[i][2])
        li[i].append(li[i][3] / 2)
    #print(li)

    print("********* 성적표 ***********")
    print("=============================")
    print(" 이름   국어  수학  총점  평균")
    print("=============================")
    for i in range(4):
        print(" {}  {}   {}   {}  {}".format(li[i][0],
                 li[i][1], li[i][2], li[i][3], li[i][4]))
    print()

    print("******* 과목별 평균 ********")
    sum_subj = [0, 0]
    for i in range(4):
        sum_subj[0] += li[i][1]
        sum_subj[1] += li[i][2]
    print(" 국어 : {0}, 수학 : {1}".format(sum_subj[0]/4, sum_subj[1]/4))
