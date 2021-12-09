
f = open('c:/pyfile/kbo2021.txt', 'r')
lines = f.readlines()  #리스트 형태로 저장
print(lines)
for line in lines:
    print(line)
f.close()
