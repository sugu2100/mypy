# 1번
국어 = 80
영어 = 75
수학 = 55
합계 = 국어 + 영어 + 수학
평균 = 합계 / 3

print("평균", 평균)

# 2번
n = 13
if n % 2 == 1:
    print('홀수')
else:
    print('짝수')

# 3번
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]

print(yyyymmdd)
print(num)

# 4번
print(pin[7])

# 5번
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6번
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7번
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8번
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9번
a = dict()

a['name'] = 'python'

a[('a',)] = 'python'
#a[[1]] = 'python'
a[250] = 'python'
print(a)

# 10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)
print(a)

# 11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
print(aSet)
b = list(aSet)
print(b)

# 12번
a = b = [1, 2, 3]
a[1] = 4
print(a)






















