# 건강 지수 클래스
class health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getname(self):
        return self.__name

    def sethp(self, hp):
        if hp < 0:
            hp = 0
        if hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return 'hp : ' + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다.".format(hours))

    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print("{}잔 마시다.".format(cups))

p1 = health("이몽룡")
p1.sethp(90)
p1.exercise(1)
p1.drink(5)
print(p1.getname(), p1.gethp())

p2 = health("성춘향")
p2.sethp(100)
p2.exercise(3)
p2.drink(1)
print(p2.getname(), p2.gethp())
