#наследование

class Person:#базовый класс (родительский - parent)

    pass


class Doctor(Person):#подкласс (subclass)

    pass


class Architect(Person):

    pass


class Mylist(list):
    pass




issubclass(Person, object)#True
m=Mylist()
print(m)#[]
m.append(78)
issubclass(m, list)#True
