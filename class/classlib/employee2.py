
class Employee:
    serial_num = 1000

    def __init__(self):
        Employee.serial_num += 1
        self.id = Employee.serial_num

    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

e1 = Employee()
e1.setname("김산")
print("사번 : " + str(e1.getid()) + ", 이름 : " + e1.getname())

e2 = Employee()
e2.setname("이강")
print("사번 : " + str(e2.getid()) + ", 이름 : " + e2.getname())

e3 = Employee()
e3.setname("박대양")
print("사번 : " + str(e3.getid()) + ", 이름 : " + e3.getname())