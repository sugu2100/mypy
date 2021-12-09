# 동명 이인 찾기
def find_same_name(a):
    same_name = set()  # 결과를 저장할 빈 집합
    #same_name = []
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(i, j)
            if a[i] == a[j]:
                same_name.add(a[i])
                #same_name.append(a[j])
    return same_name

name = ["홍길동", "이순신", "성춘향", "이몽룡", "이순신", "성춘향"]
result = find_same_name(name)
print(result)
