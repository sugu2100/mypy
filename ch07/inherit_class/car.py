class Car:
    def drive(self):
        print("차가 주행합니다.")

class Taxi(Car):
    def drive(self):
        print('택시가 주행합니다.')

class Bus(Car):
    def drive(self):
        print('버스가 주행합니다.')

taxi = Taxi()
taxi.drive()

bus = Bus()
bus.drive()
