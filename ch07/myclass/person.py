class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    p1 = Person("홍길동", 30)
    p2 = Person("성춘향", 20)
    print(p1.name)
    print(p1.age)
    print(p2.name)
    print(p2.age)
