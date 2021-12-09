# 이차원 리스트에서 'c'를 출력하기
'''
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[3][2])
print(a[3][:2])

print(a[3][0:2])
print(a[4])
'''

d1 = [1, 2, 3]

d1.append(4)
print(d1)

d2 = [[80], [90], [100]]
d2.append([70])
print(d2)

# 리스트를 출력
for i in d2:
    print([i][0], end=' ')
print()

for x in d2:
    print(x)

'''
# 리스트 안의 값을 출력
#n = len(d2)
for i in range(len(d2)):
    for j in range(len(d2[i])):
        print(d2[i][j], end=' ')
    print()
print()


# 합계
total = 0
for i in range(len(d2)):
    for j in range(len(d2[i])):
        total += d2[i][j]
    print()
d2.append([total])

print(d2)
'''











