
from classlib.car import Car

car1 = Car("아반떼", "silver", 2000)
car2 = Car("소나타", "blue", 2500)

print("\t 모델명\t색상\t\t배기량")
print("car1 " + car1.model + "\t" + car1.color + "\t" + str(car1.cc))
print("car2 " + car2.model + "\t" + car2.color + "\t" + str(car2.cc))
