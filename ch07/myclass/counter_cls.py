# 클래스 변수
class Counter:

    x = 0  # 클래스 변수

    def __init__(self):
        Counter.x += 1

    def showinfo(self):
        print(self.x)


c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()
