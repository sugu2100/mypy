# 재귀 호출
def sos(i):
    print("help me!")
    if i <= 1:  # 가장 작은 횟수 처리
        return ""
    else:
        return sos(i-1)

sos(5)  #help me!
#sos(4) #help me!
#sos(3) #help me!
#sos(2) #help me!
#sos(1) #help me!
#공백을 출력하고 종료
