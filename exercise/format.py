"""
# 문자열 포매팅
print("I eat %d apples" % 3)
print("I eat %s apples" % 'five')

number = 5
print("I eat %d apples" % number)
day = 3
print("I ate %d apples. so I was sick for %s days" % (number, day))

# format() 함수
print("I eat {0} apples".format(3))

n = 5
print("I eat {0} apples".format(n))
day = 2
print("I ate {0} apples. so I was sick for {1} days".format(n, day))

# split()

s = 'grape banana peach'
s = s.split(' ')
print(s)
"""

n1, n2 = input("두 수 입력 : ").split(' ')
x = int(n1)
y = int(n2)
times = x * y
print(times)

n = input("세 수 입력 : ")
li = n.split()
print(li)

total = 0
for i in li:
    total += int(i)

print("합계 :", total)























