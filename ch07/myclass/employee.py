# 사번 자동 발급
class Employee:
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def showinfo(self):
        print(self.getid(), self.getname())

e1 = Employee("김산")
e1.showinfo()
e2 = Employee("이강")
e2.showinfo()
e3 = Employee("해찬들")
e3.showinfo()
