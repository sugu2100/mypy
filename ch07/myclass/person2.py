class Person:
    def __init__(self):  #초기자, 생성자 함수
        self.__name = "홍길동"
        self.__age = 30

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

p = Person()
print(p.getname())
print(p.getage())
