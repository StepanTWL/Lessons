#наследование

class Person:#базовый класс (родительский - parent)

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):#подкласс (subclass)

    def can_cure(self):
        print('Я могу лечить')


class Architect(Person):

    def can_build(self):
        print('Я могу построить здание')


class Ortoped(Doctor):
    pass

d = Doctor()
a = Architect()
a.can_build()
a.can_breathe()
a.can_walk()
d.can_cure()
d.can_breathe()
d.can_walk()
print(issubclass(Doctor, Person))#True
print(isinstance(d, Doctor))#True
print(isinstance(d, Architect))#False
print(isinstance(d, Person))#True
