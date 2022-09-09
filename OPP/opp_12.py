#магические методы __add__, __mul__, __sub__, __truediv__

class BankAccount:

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.balance*other
        if isinstance(other, BankAccount):
            return self.balance*other.balance
        raise NotImplemented

    def __radd__(self, other):
        return self+other

    def __rmul__(self, other):
        return self*other



a = BankAccount('Misha', 500)
b = BankAccount('Tanya', 500)
print(a+500)#1000 делает новый экземпляр(объект под тем же именем)
print(a+b)#1000
print(500+a)#1000
print(a*500)#250000
print(a*b)#250000
print(500*a)#250000