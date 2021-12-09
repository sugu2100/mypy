
def divide(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다.")
    finally:
        print("여기는 반드시 수행되는 구간입니다.")

#divide(2, 1)
divide(2, 0)

