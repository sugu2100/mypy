# 전역변수의 유효 범위
def one_up():
    #global x  #x를 전역변수로 사용한다는 의미
    x = x + 1
    print("y = %d" % x)

x = 0
one_up()
one_up()

