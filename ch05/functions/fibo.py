# 피보나치 수열 - 1, 1, 2, 3, 5...

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(1))  #1
print(fibo(2))  #1
print(fibo(3))  #1+1
print(fibo(4))  #1+1+1
print(fibo(5))  #1+1+1+1+1
print(fibo(6))  #1+1+1+1+1+1+1+1
