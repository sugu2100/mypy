
def negative(a):
    li = []
    for i in a:
        if i < 0:
            li.append(i)
    return li

v = [-5, 1, 2, -11, 76]
print(negative(v))

#lambda - filter() 함수
negative2 = lambda x : x < 0
result = filter(negative2, v)
print(list(result))
