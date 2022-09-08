from typing import Union


class BankAccount:

    def __init__(self, name: str, balance: Union[int, float]) -> None:
         self.name = name
         self.__balance = balance
        
    @property
    def my_balance(self) -> Union[int, float]:
        return self.__balance

    @my_balance.setter
    def my_balance(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self) -> None:
        del self.__balance
    
    

