# 전역변수의 유효 범위
def price():
    price = 250 * quantity
    print("{}원입니다.".format(price))

quantity = 2;
print("{0}개에".format(quantity))
price()

