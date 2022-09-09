#магические методы (dunder) __str__, __repr__, __len__, __abs__

class Lion:

    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return f"The object Lion - {self.name}"

    def __str__(self) -> str:
        return f"Lion - {self.name}"


s = Lion('Simba')
print(s)#The object Lion - Simba

print(s)#Lion - Simba


class Person:

    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def __len__(self):# не может выдавать числа < 0 (проверка самого питона)
        return len(self.name+self.surname)

    def __abs__(self):
        return abs(self.age)


class Otrezok:
    def __init__(self, point1, point2) -> None:
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self) # == self.__abs__()

    def __abs__(self):
        return abs(self.x1 - self.x2)