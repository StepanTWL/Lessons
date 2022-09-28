#инструкция raise
"""try:
    [1,2,3][15]
except (KeyError, IndexError) as error:
    print(f"Logging error: {repr(error)}")
    raise TypeError('ошибка типа') from None

try:
    raise ValueError('ошибка значения')
except ValueError as first:
    try:
        raise TypeError('ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from first
"""

#Пользовательские исключения
class MyException(Exception):
    """this is my first Exceptic"""

    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self) -> str:
        print('str call')
        if self.message:
            return f"MyException ({self.message})"
        else:
            return "MyException is empty"

try:
    raise MyException('hello', 1, 2, 3)
except AttributeError:
    print('done')


class SnakeExceptionBase(Exception):
    """Основной класс ошибок змейки"""

class SnakeBorderException(SnakeExceptionBase):
    """Ошибка соприкосновения змеи со стенкой"""

class SnakeTailException(SnakeBorderException):
    """Соприкосновение змеи и тела"""