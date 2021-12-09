
class Employee:
    def __init__(self):
        self.empid = int(input("사번 : "))
        self.name = input("이름 : ")

    def __str__(self):
        return "{}  {}".format(self.empid, self.name)

li = []
for i in range(3):
    li.append(Employee())

print("사번   이름")
for i in li:
    print(i)

