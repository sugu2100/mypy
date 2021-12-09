# 매개 변수가 있는 초기자
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("학생이 배웁니다.")

    def __str__(self):
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)
    """
    def showInfo(self):
        print("학생 이름은 " + self.name + "이고, "
                    + str(self.grade) + "학년입니다.")
    """

if __name__ == "__main__":
    s1 = Student("콩쥐", 1)
    print(s1)
    s1.learn()

    s2 = Student("팥쥐", 2)
    print(s2)
    s2.learn()
