from ch07.class_lib.customer import Customer

class GoldCustomer(Customer):    # Customer를 상속
    def __init__(self, cid, name):
        super().__init__(cid, name)  # 부모 멤버 상속
        self.cgrade = "GOLD"         # 골드 등급
        self.sale_ratio = 0.1        # 구매 할인율
        self.bonus_ratio = 0.02      # 보너스 적립율

    def calc_price(self, price):  # 부모 메서드(함수) 재정의
        price -= int(price * self.sale_ratio)
        # 할인된 가격 = 가격 - (가격 x 구매할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        # 보너스 포인트 = 할인된 가격 x 보너스 적립율
        return price
