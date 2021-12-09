
d1 = [1, 2, 3]
d2 = [
        [80],
        [90],
        [100]
]

d1.append(10)   # 1차원 리스트는 값을 추가
print(d1)
"""
print(d2[0][0])
print(d2[1][0])
print(d2[2][0])

for i in d2:
    print([i][0], end=' ')
"""

d2.append([70], [80])  # 이차원 리스트는 리스트를 추가
print(d2)

sum = d2[0][0] + d2[1][0] + d2[2][0]
d2.append([sum])  # 합계를 구하여 추가
avg = (d2[0][0] + d2[1][0] + d2[2][0]) / 3
d2.append([avg])  # 평균을 구하여 추가
print(d2)
