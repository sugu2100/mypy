
class AirPlane:

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")


class SuperSonicAirPlane(AirPlane):
    NORMAL = 1        # 클래스 상수 - 대문자
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("초음속으로 비행합니다.")
        else:
            super().fly()


sa = SuperSonicAirPlane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirPlane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirPlane.NORMAL
sa.fly()
sa.land()

