
class Cart:
    li = []  # 클래스 리스트

    def __init__(self, goods):
        Cart.li.append(goods)

    def __str__(self):
        print(Cart.li)

c1 = Cart("계란")
print(c1.li)
c2 = Cart("두부")
print(c2.li)
c3 = Cart("커피")
print(c3.li)
