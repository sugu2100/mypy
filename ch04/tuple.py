# 튜플
t1 = ()  # 빈 튜플
t2 = (1, ) # 1개 추가시, 쉼표를 넣음
t3 = (2, 3, 4)

print(t1)
print(t2)
print(t2 + t3)

t1 = ('국화', '코스모스', '매화')
print(t1)

# 인덱싱
print(t1[0:2])
print(t1[-1])
print(t3[1:2])

# 변경, 삭제 불가
t3[0] = 10
del t3[1]

