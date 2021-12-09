# 한 사람만 만들 수 있음
class Student:
    def __init__(self):
        print("생성자 함수입니다.")
        self.name = "콩쥐"
        self.grade = 2

    def learn(self):
        print("학생이 배웁니다.")

s = Student()
print(s.name)
print(s.grade)
s.learn()
