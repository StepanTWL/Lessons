from typing import Union


class Square:

    def __init__(self, s: Union[int, float]) -> None:
        self.__side = s
        self.__area = None

    @property
    def side(self) -> Union[int, float]:
        return self.__side

    @side.setter
    def side(self, value: Union[int, float]) -> None:
        self.__side = value
        self.__area = None

    @property
    def area(self) -> Union[int, float]:
        if self.__area is None:
            self.__area = self.side**2
        return self.__area

d = Square(6)
d.area#36
d.side = 3
d.area#9