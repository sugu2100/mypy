# 파일 쓰기
with open('hello.txt', 'w') as f:
    f.write('Hello~ \n')
    f.write('안녕~ \n')
    num = "1 inch는 %.2fcm" % 2.54
    f.write(num)

with open('hello.txt', 'r') as f:
    #data = f.read()
    data = f.readlines()
    #print(data)
    for i in data:
        print(i, end='')

