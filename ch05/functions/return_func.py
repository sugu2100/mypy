# 두 수를 매개변수로 전달하여 같으면 곱하고, 다르면 더하는 함수

def data(x, y):
    if x == y:
        return x * y
    else:
        return x + y

n1 = data(5, 5)
n2 = data(10, 5)

print("n1 = %d" % n1)
print("n2 = %d" % n2)
