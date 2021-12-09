
def some_function():
    num = int(input("1~10 사이의 수를 입력하세요 : "))
    if num < 1 or num > 10:
        raise Exception("예외가 발생했습니다.")
    else:
        print("입력한 수는 {}입니다.".format(num))

try:
    some_function()
except Exception as e:
    print(e)