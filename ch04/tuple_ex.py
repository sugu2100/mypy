# tuple 생성 및 관리
t1 = ()    #빈 튜플
print(t1)

t1 = (1, ) # 1개 추가시 콤머를 붙임
print(t1)
print(type(t1)) 

'''
t1 = (1)
print(t1)
print(type(t1)) - 정수
'''

t2 = (2, 3, 4)
print(t2)

#요소 추가 - 초기화나 튜플 합하기
t1 = t1 + t2
print(t1)
print(t2)

# 인덱싱과 슬라이싱
print(t2[0])
print(t2[0:])
print(t2[0:-1])
print(t2[1:2])

#수정 불가
#t2[2] = 5

#삭제 불가
#del t2[1]











