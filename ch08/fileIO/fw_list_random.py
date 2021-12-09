import random

try:
    f = open('2021kbo.txt', 'r')
    data = f.read().split()
    #print(data)
    team = random.choice(data)
    print(team)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
