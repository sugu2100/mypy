
f = open('c:/pyfile/kbo2021.txt', 'w')

team = ['NC', '키움', '기아', '삼성', '롯데', 'LG', 'KT', 'SSG']
for i in team:
    f.write(i + ' ')
f.close()

f = open('c:/pyfile/kbo2021.txt', 'r')

data = f.read()
print(data)
f.close()