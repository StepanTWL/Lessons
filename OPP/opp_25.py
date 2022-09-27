#Множественное наследование

class Doctor:

    def __init__(self, degree) -> None:
        self.degree = degree

    def gradate(self):
        print('ura doctor')

    def can_cure(self):
        print('can cure')


class Builder:

    def __init__(self, rank) -> None:
        self.rank = rank

    def gradate(self):
        print('ura builder')

    def can_build(self):
        print('can build')

    def can_cure(self):
        print('can cure too')


class Person(Doctor, Builder):#MRO method resolushin order порядок поиска методов и свойств

    def __init__(self, degree, rank) -> None:
        Doctor.__init__(self, degree)
        Builder.__init__(self, rank)

    def gradate(self):
        print('who am i')
        super().gradate()
        Doctor.gradate(self)

    def __str__(self) -> str:
        return f"Person {self.rank} {self.degree}"

    def can_build(self):
        print('can build too')


s = Person(5, 'spec')
s.can_build()#can build too
s.can_cure()#can cure
print(Person.__mro__)#(<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>) порядок поиска методов и свойств
s.gradate()#who am i      ura doctor
print(s)#Person spec 5