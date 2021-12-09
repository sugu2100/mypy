# 단위 변환 클래스 만들기
# inch를 mm로 변환하기 : 1inch -> 25mm
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from   # 단위
        self.units_to = units_to       # 변환할 단위
        self.factor = factor           # 변환 값

    def convert(self, value):  # 변환 계산 함수
        return self.factor * value  # 단위 기본값 x 수

if __name__ == "__main__":
    c = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    print(str(c.convert(2)) + c.units_to)

