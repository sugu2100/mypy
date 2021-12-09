# 배송비 계산하기
def price(unit_price, quantity):
    delivery_fee = 2500            # 배송비
    price = unit_price * quantity  #상품가격 = 단위당 가격 * 수량
    if price < 20000:
        price += delivery_fee
        return price
    else:
        return price

price1 = price(15000, 2)   #price 함수 호출
price2 = price(5000, 3)
print("상품1 가격은 " + str(price1) + "원입니다.")
print("상품2 가격은 " + format(price2, ',') + "원입니다.")

