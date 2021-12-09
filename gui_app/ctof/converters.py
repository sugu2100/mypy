
class Converters:
    def __init__(self, units_from, units_to, factor, offset):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor
        self.offset = offset

    def convert(self, value):
        return self.factor * value + self.offset

if __name__=="__main__":
    c = Converters('C', 'F', 1.8, 32)
    print(str(c.convert(20)) + c.units_to)

    