#파일 읽기
f = open("C:/pyfile/hello.txt", "r")
data = f.readlines()
print(data)
for i in data:
    print(i, end='')
f.close()


