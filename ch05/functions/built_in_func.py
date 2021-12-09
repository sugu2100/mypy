# 내장 함수
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

print(any([1, 2, 0]))

# 문자열 -> 숫자로 변환
print(eval('1+2'))

# 리스트로 반환
print(list('python'))

# 반올림
print(round(4.6)) #5
print(round(4.5)) #4

# 합계
print(sum([1, 2, 3, 4]))  #10

# 최소값
print(min([11, 40, 97, 2, 65]))

# 거듭 제곱
print(pow(2, 4))

def my_pow(x, y):
    num = 1
    for i in range(0, y):
        num *= x
    return num

print(my_pow(2, 4))
