# 구구단 3단의 결과값
def gugu(n):
    li = []
    for i in range(1, 10):
        li.append(n * i)
        print(li)
    return li

print(gugu(3))
