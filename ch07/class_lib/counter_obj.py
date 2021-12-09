
class Counter:
    def __init__(self):
        self.x = 0
        self.x += 1

    def get_count(self):
        return self.x

c1 = Counter()
print(c1.get_count())   # 1
c2 = Counter()
print(c2.get_count())   # 1
c3 = Counter()
print(c3.get_count())   # 1
