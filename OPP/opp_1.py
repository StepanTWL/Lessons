class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive() -> None:
        print("Let's go!")

print(Car.__dict__)

a = Car()
print(getattr(a, 'mass', 1500))#выдает значеие атрибута и если его нет подставяет число
a.model = "AUDI"
a.mass = 1500
#setattr(a, 'mass', 1500)тоже что и выше
del a.mass
#delattr(a, 'mass')тоже что и 

#Добавление/убавление атрибутов в классе так же затрагивает и экземпляры этого класса!!!
a1 = Car()
a2 = Car()
a1.seat = 4
a1.model = 'AUDI'
print(a1.__dict__)#{'seat': 4, 'model': 'AUDI'}
del a1.model
print(a1.model)#bmw
Car.drive()#Let's go!
getattr(Car, 'drive')()#Let's go!
a1.drive()#можно использовать только при наличии @staticmethod
pass