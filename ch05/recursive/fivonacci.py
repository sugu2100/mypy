# fivonacci 수열 - 재귀함수
# 1, 1, 2, 3, 5, 8....
def fibo(n):
    global count
    count += 1
    if n<=2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

count = 0
print(fibo(12))
print(fibo(35))  # 계산이 복잡함
print(count)
