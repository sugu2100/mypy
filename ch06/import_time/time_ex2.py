import time

# 수행 시간 측정하기
start = time.time()

# 1초 간격으로 출력
for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print("수행 시간 : " + str(end-start) + "초" )




