# 거듭 제곱 - 밑과 지수
power = lambda x, y : x ** y

print(power(2,2))
print(power(2,3))
print(power(2,4))

# map()
li = [1, 2, 3, 4, 5, 6]
li2 = []
li3 = []

times = lambda x : x * 2
li2 = map(times, li)  # li에 일치되는 요소를 저장
print(list(li2))   # 리스트 형태로 출력

print(list(map(lambda x : x * 2, li))) # 한 줄에 코딩

# filter()
smaller = lambda x : x < 4
li3 = filter(smaller, li)   # li에서 추출하여 저장
print(list(li3))

print(list(filter(lambda x : x < 4, li))) # 한 줄에 코딩
