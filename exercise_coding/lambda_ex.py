
def call_10(func):
    for i in range(10):
        func()

def hello():
    print("안녕하세요")

call_10(hello)
print('='*20)

# lambda
hello2 = lambda : print("안녕하세요")
call_10(hello2)