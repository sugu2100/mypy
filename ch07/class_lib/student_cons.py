
class Student:
    def __init__(self, name, grade): # 생성자 함수(매개 변수)
        self.name = name      # 멤버 변수에 매개변수 저장
        self.grade = grade

    def learn(self):
        print("수업을 듣습니다.")

s1 = Student("김하나", 1)  # 이름과 학년을 인자로 전달하여 객체 생성
print(s1.name + " 학생은 " + str(s1.grade) + "학년입니다.")
s1.learn()

s2 = Student("이두울", 2)
print(s2.name + " 학생은 " + str(s2.grade) + "학년입니다.")
s2.learn()

