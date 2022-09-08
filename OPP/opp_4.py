class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self) -> None:
        self.__dict__ = Cat.__shared_attr

a = Cat()
a.name = 'Tom'


class BankAccount:

    def __init__(self, name: str, balance: int, passport: int) -> None:
        self.name = name#public
        self._balance = balance#protected - защищенные
        self.__passport = passport#privat

    def print_for_root(self) -> None:
        self.__print_all_data()

    def print_protected_data(self) -> None:
        print(self.name, self._balance)

    def print_private_data(self) -> None:#инкапсуляция
        print(self.name, self._balance, self.__passport)

    def __print_all_data(self) -> None:
        print(self.name, self._balance, self.__passport)

account1 = BankAccount('Bob', 100000, 30678)
account1.print_protected_data()#'Bob' 100000
account1.print_private_data()#'Bob' 100000 30678
print(account1._balance)#подчеркивание усно указывает что это зачисщенные данные и использовать их за рамками класса запрещено
#print(account1.__passport)#error
account1.print_for_root()
#account1.__print_all_data()#error

##Хитрость!!!##
#как получить доступ к private
account1._BankAccount__print_all_data()


####### Почитать про модуль accessify для полной защиты данных######