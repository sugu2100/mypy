class Cart:
    li = []

    def __init__(self, goods):
        Cart.li.append(goods)

    def showinfo(self):
        print(self.li)

c1 = Cart('계란')
c1.showinfo()
c2 = Cart('두부')
c2.showinfo()
c3 = Cart('커피')
c3.showinfo()
