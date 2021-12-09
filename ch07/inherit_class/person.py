# Person 클래스

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #객체의 정보 문자열로 출력하는 함수
        return "이름 : {}, 나이 : {}".format(self.name, self.age)

if __name__=="__main__":
    p = Person("김하늘", 21)  # p객체 생성
    print(p)

