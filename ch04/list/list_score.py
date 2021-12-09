# 리스트 추가, 조회, 수정, 삭제
score = [ 10, 20, 30, 40 ]

# 수정
score[1] = 50
print(score)

# 삭제
del score[2]
print(score)

# 요소 추가 - append 함수
score.append(60) # 맨 뒤로 추가
print(score)
score.insert(1, 20) # 1번 위치에 추가
print(score)

# 요소 삭제
score.remove(50)
print(score)

# 요소의 개수
print(len(score))

