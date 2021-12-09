# 문자열 함수

s = "a:b:c:d"
s = s.split(':')
print(s)

'''
n1, n2 = input("두 수 입력 : ").split()
add = int(n1) + int(n2)
print(add)

n = input("세 수 입력: ")
li = n.split()
print(li)

tot = 0
for i in li:
    tot = tot + int(i)

print("합계 : " , tot)
'''

str2 = "  hi, soo   "
str2 = str2.strip()
print(str2)

s = "Hello, Korea"
print(s.replace("Korea", "incheon"))

x = '123'.isnumeric()
print(x)

x = '123A'.isnumeric()
print(x)
















