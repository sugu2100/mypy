from ch07.class_lib.goldcustomer import GoldCustomer
from ch07.class_lib.customer import Customer
from ch07.class_lib.vipcustomer import VIPCustomer

s = Customer(101, "놀부")           #Customer 객체 생성
g = GoldCustomer(201, "흥부")       #GlodCustomer 객체 생성
v = VIPCustomer(301,"심청이", 1234) #VIPCustomer 객체 생성

# 상품 가격 계산
cost_s = s.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(10000)

# 제품 지불 비용 출력
print(s.getname() + "님의 지불비용은 " + str(cost_s) + "원 입니다.")
print(g.getname() + "님의 지불비용은 " + str(cost_g) + "원 입니다.")
print(v.getname() + "님의 지불비용은 " + str(cost_v) + "원 입니다.")

# 고객 정보
print(s)
print(g)
print(v)


