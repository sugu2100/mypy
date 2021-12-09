#파일 쓰기
f = open("C:/pyfile/repeat.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

#파일 읽기
f = open("C:/pyfile/repeat.txt", 'r')

text = f.read()
print(text)
f.close()
