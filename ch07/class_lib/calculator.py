# 계산기 클래스 정의 및 사용
class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x += y
        return self.x

    def sub(self, y):
        self.x -= y
        return self.x

c = Calculator()
print(c.add(10))  # 10을 더하기
print(c.sub(4))   # 4를 빼기

