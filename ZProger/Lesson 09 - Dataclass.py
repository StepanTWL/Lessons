from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int

    def get_name(self):#не жалательно в датаклассах использовать функции
        print(self.name)

def test(user: User):
    pass

a = User('1', 1)
a.get_name()

class UserHandle:
    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, value):
        self.user.__dict__[key] = value


b = UserHandle('alex', 25)
print(b)#<__main__.UserHandle object at 0x0000000000619640>
print(b.__dict__)#{'user': User(name='alex', age=25)}
print(b.get_dataclass())#{'name': 'alex', 'age': 25}
