# Employee 클래스
class Employee:
    serial_num = 1000  #기준값 (클래스 변수)

    def __init__(self):
        Employee.serial_num += 1      # serial_num을 1증가
        self.id = Employee.serial_num # id에 serial_num 저장

    def get_id(self):
        return self.id

    def set_name(self, name):   # name을 매개변수로 전달
        self.name = name

    def get_name(self):
        return self.name

    