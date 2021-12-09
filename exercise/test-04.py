# 1번
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

result = is_odd(12)
print(result)

# 2번
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
        #print(i, result)
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1,2,3,4,5))

# 3번
"""X
input1 = input("첫번째 숫자: ")
input2 = input("두번째 숫자: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)
"""

# 5번
f1 = open("C:/test/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("C:/test/test.txt", 'r')
data = f2.read()
print(data)
f2.close()

# 6번
"""
user_input = input("저장할 내용을 입력하세요: ")
f = open('input.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()
"""

# 7번
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()