#Наследование делегирование Delegating

class Person:

    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def breathe(self):
        print('person breathe')


class Doctor(Person):

    def __init__(self, name, surname, age) -> None:
        super().__init__(name, surname)
        self.age = age

    def breathe(self):
        print('doctor breathe')
        super().breathe()#брать метод из родительского класса

p = Person('Ivan', 'Ivanov')
d = Doctor('Ivan', 'Ivanov', 25)