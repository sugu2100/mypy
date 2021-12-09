# 점수 리스트 선언 및 생성
score = [70, 80, 50, 60, 90, 40]

# 오름차순 정렬
n = len(score)
for i in range(0, n):  
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]

        '''
        # 1행
          70, 50, 60, 80, 40, 90
        # 2행
          50, 60, 70, 40, 80, 90
        # 3행
          50, 60, 40, 70, 80, 90
        # 4행
          50, 40, 60, 70, 80, 90
        # 5행
          40, 50, 60, 70, 80, 90

        '''
for i in score:
    print(i)
    
