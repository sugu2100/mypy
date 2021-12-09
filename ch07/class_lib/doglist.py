# 클래스 변수와 인스턴스 변수
class Dog:
    #tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []   # trick 멤버 리스트

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("kit")
dog2 = Dog("elsa")

dog1.add_trick('roll over')
print(dog1.tricks)  # unique roll over

dog2.add_trick('play dead')
print(dog2.tricks)  # unique play dead
