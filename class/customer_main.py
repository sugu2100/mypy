
from classlib.customer import Customer, GoldCustomer, VIPCustomer

s1 = Customer(101, "흥부")
s2 = Customer(102, "놀부")
g1 = GoldCustomer(201, "콩쥐")
g2 = GoldCustomer(202, "팥쥐")
vip1 = VIPCustomer(301, "심청", 123)

# 리스트로 관리
customers = []
customers.append(s1)
customers.append(s2)
customers.append(g1)
customers.append(g2)
customers.append(vip1)

print("===== 구매 가격과 보너스 포인트 계산 =====")
price = 10000
for customer in customers:
    cost = customer.calc_price(price)   # 구매 가격(지불 금액)
    print(customer.getname() + "님의 지불 금액은 " + format(cost, ',d') + "원 입니다.")

print("========== 고객 정보 출력 ==========")
for customer in customers:
    customer.showInfo()
