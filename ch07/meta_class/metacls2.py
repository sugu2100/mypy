class MakeCalc(type):    # type을 상속받음
    # 새 클래스를 만들 때 호출되는 메서드
    def __new__(metacls, name, bases, namespace):
        # 새 클래스에 속성 추가
        namespace['desc'] = '계산 클래스'
        # 새 클래스에 메서드 추가
        namespace['add'] = lambda self, a, b : a + b
        # type의 __new__ 호출
        return type.__new__(metacls, name, bases, namespace)

Calc = MakeCalc('Calc', (), {})
c = Calc()
print(c.desc)
print(c.add(3, 4))
