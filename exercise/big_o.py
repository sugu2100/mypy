
# Big O 표기
# 1부터 n까지 합계 구하기
def sum_n(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v

print(sum_n(10))

# 방법 2
def sum_n2(n):
    sum_v = (n * (n + 1)) // 2
    return sum_v

print(sum_n2(10))


# 동명 이인 찾기
def find_same_name(li):
    same_name = []
    n = len(li)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if li[i] == li[j]:
                same_name.append(li[i])
    return same_name
'''
1행 li[0] == li[1], li[0] == li[2], li[0] == li[3], li[0] == li[4]
2행 li[1] == li[2], li[1] == li[3], li[1] == li[4]
3행 li[2] == li[3], li[2] == li[4](중복!)
4행 li[3] == li[4]
5행 li[4] 비교 대상 없음
'''
name = ['콩쥐', '팥쥐', '흥부', '놀부', '흥부']
result = find_same_name(name)
print(result)









