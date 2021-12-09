# 최대값 구하기
def find_max(a):
    max = a[0]
    for i in a:
        if max < i:
            max = i
    return max

# 최대값의 위치 구하기
def find_max_idx(a):
    max_idx = 0
    n = len(a)
    for i in range(1, n):
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx

v = [70, 80, 55, 60, 90, 40]
print(find_max(v))
print(find_max_idx(v))


   




