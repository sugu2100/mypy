

try:
    f = open("C:/pyfile/2021kb0.txt", 'r')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
