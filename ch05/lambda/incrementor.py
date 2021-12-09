# 함수를 매개 변수로 전달
print("콜백(callback) 함수")
def call_10(func):
    for i in range(10):
        func()

def hello():
    print("안녕하세요")

# 호출
call_10(hello)

# lamba 함수로 정의 - 매개변수가 없는 경우
hello2 = lambda : print("안녕하세요")
call_10(hello2)

