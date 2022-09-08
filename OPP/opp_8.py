from string import digits


class User:

    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password#будет использован метод password() перед сохранением значения
        self.__secret = 'dfsdfsdfw'

    @property
    def secret(self) -> str:
        s = input('Введите ваш пароль: ')
        if s==self.__password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self) -> str:
        return self.__password
    
    @staticmethod
    def is_include_number(password: str) -> bool:
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Значение пароля не строка')
        if len(value)<4:
            raise ValueError('Длина пароля слишком мала')
        if len(value)>24:
            raise ValueError('Длина пароля слишком велика')
        if not self.is_include_number(value):
            raise ValueError('Пароль не содержит цифры')
        self.__password = value

vasya = User('Vasya', 'dddd1')
vasya.password = 'lolp1'
print(vasya.secret)