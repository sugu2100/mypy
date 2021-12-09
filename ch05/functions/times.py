# 3의 배수와 3의 배수의 개수
def times(x):
    global count
    for i in range(1, 20):
        if i % x == 0:
            count += 1
            print(i, end=' ')
    return count

count = 0
times(3)
print()
print("배수의 개수 : %d" % count)
