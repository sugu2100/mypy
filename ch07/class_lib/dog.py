# 클래스 변수와 인스턴스 변수
class Dog:
    kind = "진돗개"

    def __init__(self, name):
        self.name = name

dog1 = Dog("백구")
dog2 = Dog("검둥이")

print(dog1.name)  # dog1만 유일(unique)
print(dog2.name)  # dog2만 유일(unique)

print(dog1.kind)   # 모든 dog이 공유(shared)
print(dog2.kind)
