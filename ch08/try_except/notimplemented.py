
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass
    '''
    def fly(self):
        print("독수리가 높이 날아갑니다.")
    '''

eagle = Eagle()
eagle.fly()
