# 구구단 곱한 값 리스트에 기억
def gugu(n):
    li = []
    for i in range(1, 10):
        li.append(n * i)
    return li

print(gugu(3))

# 3과 5의 배수의 합과 개수
sum_v = 0
count = 0
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        sum_v += i
        count += 1
        print(i, end=' ')
print()
print("합계 :", sum_v)
print("개수 :", count)

# 게시판 페이지 수 계산하기
def getpage(x, y):
    if x % y == 0:
        page = x // y
    else:
        page = x // y + 1
    return page

print(getpage(5, 10))
print(getpage(10, 10))
print(getpage(15, 10))
print(getpage(20, 10))
