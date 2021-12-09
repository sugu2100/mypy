class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def showinfo(self):
        print(self.sid, self.name)


s1 = Student(1001, '김산')
s1.showinfo()
s2 = Student(1002, '이강')
s2.showinfo()
s3 = Student(1003, '박대양')
s3.showinfo()
