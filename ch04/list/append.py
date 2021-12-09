# 배열의 복사
a = [1, 2, 3, 4, 5, 6]
a2 = []

for i in a:
    a2.append(i)

print(a2)

# 홀수를 저장하는 리스트 
a3 = []
for i in a:
    if i % 2 == 1:
        a3.append(i)

print(a3)

# a리스트의 요소에 3을 곱하여 저장하는 리스트
a4 = []
for i in a:
    a4.append(i * 3)

print(a4)       

# 리스트 내포
a5 = []
a5 = [i * 3 for i in a]
print(a5)
