
f = open('2021kbo.txt', 'w')
team = ['NC', '키움', '기아', '삼성', '롯데', 'LG', 'KT', 'SSG']
"""
for i in team:
    f.write(i + ', ')
"""
for i in range(len(team)):
    f.write(team[i] + " ")
f.close()

f = open('2021kbo.txt', 'r')
#data = f.read()
data = f.read().split()
print(data)
f.close()
