
try:
    a = [1, 2]
    print(a[2])
    4 / 0

except IndexError as e:
    print(e)
    #print("범위를 벗어났습니다.")
except ZeroDivisionError as e:
    print(e)
    #print("0으로 나눌 수 없습니다.")

