from ch07.class_lib.scaleconverter import ScaleConverter
# 단위 변환 클래스 - 온도 변환
# F(화씨온도) = C(섭씨온도) * 1.8 + 32
class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)  #부모 클래스 멤버 상속
        self.offset = offset   # 단위 값

    def convert(self, value):
        return self.factor * value + self.offset  # (단위1 값 x 수) + 단위2 값

con = Converter('C', 'F', 1.8, 32)
print("Converting 20C")
print(str(con.convert(20)) + con.units_to)
