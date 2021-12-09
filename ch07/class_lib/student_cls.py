
class Student:
    def __init__(self):
        self.name = "콩쥐"   # 멤버 변수
        self.grade = 1
        print("생성자 함수")

    def learn(self):        # 멤버 함수
        print("수업을 듣습니다.")

s = Student()   # s는 Student 클래스의 객체(인스턴스)
print(s.name + " 학생은 " + str(s.grade) + "학년입니다.")
s.learn()
