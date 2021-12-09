# 리스트 생성 및 사용
seasons = ["봄", "여름", "가을", "겨울"]

# 1개 출력(인덱싱)
print(seasons[0])
print(seasons[-1])

# 리스트 출력
print(seasons)
print(type(seasons))

# 슬라이싱
# [0:n] -> n-1 위치
print(seasons[0:3])  
print(seasons[:3])   
print(seasons[2:4])
print(seasons[2:])

# 전체 요소 출력
for i in seasons:
    print(i)

