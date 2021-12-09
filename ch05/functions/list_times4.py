# 리스트에서 새로운 리스트 만들기
def times(a):
    li = []
    for i in a:
        li.append(i * 4)
    return li

v = [ 1, 2, 3, 4]
print(times(v))
