# 장바구니 클래스
class Cart:
    li = []   #클래스 리스트

    def __init__(self, goods):
        Cart.li.append(goods)
        # 클래스 이름으로 직접 접근

    def __str__(self):
        return Cart.li

cart1 = Cart("계란")  #계란 추가
#print(cart1.li)
cart2 = Cart("두부")  #두부 추가
#print(cart2.li)
cart3 = Cart("커피")  #커피 추가
print(cart3.li)


