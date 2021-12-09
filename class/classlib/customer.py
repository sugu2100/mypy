
class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.cgrade = "Silver"
        self.bonus_point = 0
        self.bonus_ratio = 0.01   # 포인트 적립율 1%

    def calc_price(self, price):
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def getname(self):
        return self.name

    def showInfo(self):
        print(self.name + "님의 등급은 " + self.cgrade +
              "이고, 보너스 포인트는 " + format(self.bonus_point, ',d') + "점 입니다.")

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name)
        self.cgrade = "GOLD"
        self.sale_ratio = 0.1     # 구매 할인율 10%
        self.bonus_ratio = 0.02   # 보너스 적립율 2%

    def calc_price(self, price):  # 재정의
        price -= int(price * self.sale_ratio) # 상품 가격 = 상품가격 - 할인가격
        self.bonus_point += int(price * self.bonus_ratio)
        return price

class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)
        self.agent = agent
        self.cgrade = "VIP"
        self.sale_ratio = 0.1
        self.bonus_ratio = 0.05   #보너스 적립율 5%

    def calc_price(self, price):
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def showInfo(self):   # 재정의
        super().showInfo()
        print("상담원 ID는 " + str(self.agent) + "입니다.")


