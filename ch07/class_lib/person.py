
class Person:
    def __init__(self):
        self._name = ""  #멤버 변수 초기화
        self._age = 0

    def setname(self, name): # _name에 접근할 setname()함수
        self._name = name

    def getname(self):
        return self._name

    def setage(self, age): # _age에 접근할 setage()함수
        self._age = age

    def getage(self):
        return self._age

    def __str__(self):
        return "이름 : {}, 나이 : {}".format(self.getname(), self.getage())

p1 = Person()
p1.setname("콩쥐")
p1.setage(17)
print(p1)

p2 = Person()
p2.setname("팥쥐")
p2.setage(18)
print(p2)
