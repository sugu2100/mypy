
class Animal:
    def cry(self):
        raise NotImplementedError
        # 구현하지 않으면 에러 발생 시킴

class Dog(Animal):
    #pass
    def cry(self):
        print("왈~ 왈~")

class Cat(Animal):
    def cry(self):
        print("야~옹 야~옹")

dog = Dog()
dog.cry()

cat = Cat()
cat.cry()

