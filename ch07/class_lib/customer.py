#Customer 클래스
class Customer:
    def __init__(self, cid, name):
        self.cid = cid            # 고객 아이디
        self.name = name          # 고객 이름
        self.cgrade = "SILVER"    # 고객 등급
        self.bonus_point = 0      # 보너스 포인트
        self.bonus_ratio = 0.01   # 보너스 적립율 1%

    def calc_price(self, price):  # 가격을 입력받아 계산하기
        self.bonus_point += int(price * self.bonus_ratio)
        #보너스 포인트 = 보너스 포인트 + (가격 x 보너스 적립율)
        return price

    def getname(self):
        return self.name

    def __str__(self):  # 고객 정보 문자열 출력
        return self.name + "님의 등급은 " + self.cgrade + \
               " 이고, 보너스 포인트는 " + str(self.bonus_point) + "점 입니다."
