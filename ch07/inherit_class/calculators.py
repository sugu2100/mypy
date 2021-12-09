from ch07.myclass.calculator import Calculator

# 제곱수 계산이 추가된 계산기
class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y

cal = MoreCalculator(2, 4)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())