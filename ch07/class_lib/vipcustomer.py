from ch07.class_lib.customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)
        self.agent = agent      # 멤버 변수 상담원 초기화
        self.cgrade = "VIP"     # VIP 등급
        self.sale_ratio = 0.1
        self.bonus_ratio = 0.05

    def calc_price(self, price):  #부모 메서드 재정의(GOLD와 동일)
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):  # 부모 메서드 재정의
        return super().__str__() + \
               "\n상담원 ID는 " + str(self.agent) + "입니다."

