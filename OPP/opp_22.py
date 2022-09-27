#наследование (переопределить родительский метод)


class Person:#базовый класс (родительский - parent)

    def __init__(self, name) -> None:
        self.name = name

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')

    def can_sleep(self):
        print('Человек спит')
    
    def combo(self):
        self.can_breathe()
        self.can_walk()
        self.can_sleep()

    def __str__(self) -> str:
        return f"Person {self.name}"

class Doctor(Person):#подкласс (subclass)

    name = 'ivan'

    def can_breathe(self):
        print('Доктор тоже дышит')

    def __str__(self) -> str:
        return f"Doctor {self.name}"


d = Doctor('adam')
p = Person('adam')
d.can_breathe()#Доктор тоже дышит
print(d.name, p.name)#adam adam
print(d, p)#Doctor adam Person adam
d.combo()

