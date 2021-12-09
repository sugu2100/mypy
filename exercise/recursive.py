# 문자 반복 출력
def hello(i):
    print("hello~", i)
    if i <= 1:
        return ""
    else:
        return hello(i-1)

hello(10)

# 팩토리얼(factorial) - 5! = 5 x 4 x 3 x 2 x 1
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

"""
  5!
  = 5 x (5-1)!
  = 5 x (5-1) x (5-2)!
  = 5 x (5-1) x (5-2) x (5-3)!
  = 5 x (5-1) x (5-2) x (5-3) x (5-4)!
"""
print(facto(1))
print(facto(5))

# fibonacci - 1, 1, 2, 3, 5, 8...
# 앞항 + 뒤항 = 항 반복
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

"""
    n = 1    fibo(1) = 1 
    n = 2    fibo(2) = 1
    n = 3    fibo(1) + fibo(2) = 2
    n = 4    fibo(2) + fibo(3) = 3
    n = 5    fibo(3) + fibo(4) = 5
"""
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
