
def times(a):
    li = []
    for i in a:
        li.append(i * 3)
    return li

v = [1, 2, 3, 4]
print(times(v))

#lambda - map() 함수
times2 = lambda x : x * 3
result = map(times2, v)
print(list(result))
