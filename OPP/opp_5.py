from typing import Union


class BankAccount:

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.__balance = balance

    def get_balance(self) -> int:
        return self.__balance

    def set_balance(self, value: int) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self) -> None:
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

account1 = BankAccount('Bob', 400)
account1.set_balance(100)
print(account1.balance)#100
account1.balance = 400
print(account1.balance)#400