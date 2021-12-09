# 속으로 20초를 세어 맞히는 프로그램
import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end - start
print("실제 시간 : %.2f초" % et)
print("차이 : %.2f초" % abs(et-20))
