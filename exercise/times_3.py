

def times(x):
    global count
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')

count = 0
times(3)
print("\n배수의 개수 : %d" % count)
