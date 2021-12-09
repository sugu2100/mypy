
f = open('c:/pyfile/kbo2021.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
