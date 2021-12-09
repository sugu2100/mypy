
class Counter:
    x = 0   # 클래스 변수

    def __init__(self):
        Counter.x += 1
        # 클래스이름으로 직접 접근

    def get_count(self):
        return self.x

c1 = Counter()
print(c1.get_count())   # 1
c2 = Counter()
print(c2.get_count())   # 2
c3 = Counter()
print(c3.get_count())   # 3
