class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):  #Person 상속 받음
    def __init__(self, name, age, employeeid):
        super().__init__(name, age)
        self.employeeid = employeeid

class Student(Person):
    def __init__(self, name, age, studentid):
        super().__init__(name, age)
        self.studentid = studentid

p = Person("한강", 25)
print(p.name, p.age)

e = Employee("남한강", 30, 301)
print(e.name, e.age, e.employeeid)

s = Student("북한산", 20, 101)
print(s.name, s.age, s.studentid)

