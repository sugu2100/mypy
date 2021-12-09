# 0+1+2+3+4+5=15
j = 0
for i in range(6):
    j += i
    print(i, end='')
    if i==5:
        print('=', end='')
        print(j)
    else:
        print('+', end='')