# lambda - map(), filter() 함수와 사용
li = [1, 2, 3, 4, 5, 6]

# 리스트 요소에 3을 곱한수 매핑
a2 = map(lambda x : x * 3, li)
print(list(a2))
print(list(map(lambda x : x * 3, li)))

# 리스트에서 4보다 작은 수 필터링
a3 = filter(lambda x : x < 4, li)
print(list(a3))
print(list(filter(lambda x : x < 4, li)))
