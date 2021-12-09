# try ~ except ~ else 구문
# 에러가 없으면 try ~ else 실행
# 에러가 있으면 try ~ except 실행
try:
    print("1번")
    with open('2021kbo.txt') as f:
        lines = f.readlines()

except:
    print("2번")

else:
    print("3번")
    for i in lines:
        print(i, end='')
