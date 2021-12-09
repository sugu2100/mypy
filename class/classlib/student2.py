# 정보 은닉 - 캡슐화 -> 접근 제한
# 멤버변수에 언더스코어를 넣으면 직접 접근할수 없음 - private
# get(), set()으로 만들면 가능함 - public
class Student:
    def __init__(self, name):
        self._name = name
        self._grade = 0

    def getname(self):
        return self._name

    def setgrade(self, grade):
        self._grade = grade

    def getgrade(self):
        return self._grade

s1 = Student("흥부")
s1.setgrade(2)
print("학생 {0}는 {1}학년 입니다.".format(s1.getname(), s1.getgrade()))
