
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("수업을 듣습니다.")

    def __str__(self):  # 멤버를 문자열로 리턴하는 함수
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)

if __name__ == "__main__":
    s1 = Student("김하나", 1)
    print(s1)
    s1.learn()

    s2 = Student("이두울", 2)
    print(s2)
    s2.learn()

