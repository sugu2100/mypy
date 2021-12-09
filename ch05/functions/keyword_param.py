# 가변 매개변수 - 변수앞에 '*' 붙임
# dictionary로 만들어짐

def print_kw(**kwargs):
    print(kwargs)

print_kw(name="지수")
print_kw(name="지수", age=9)


