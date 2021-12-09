# 구구단 - 단을 입력받아 구구단 출력
x = int(input("단을 입력하세요 : "))
dan = int(x)

for i in range(1, 10):
    #print(dan, 'x', i, '=', dan*i)
    print("%d x %d = %d" % (dan, i, dan*i))

# 구구단 전체
for i in range(1, 10):
    print("[", i, "단]")
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j))
    print()



