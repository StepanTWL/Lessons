#Slots


from turtle import color


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

p1 = Point(3,4)
p1.q=5
p2=PointSlots(3,4)
#p2.q=5 error
del p2.y
p2.y = 50
s1 = Point(3,4)
s2 = PointSlots(3,4)
print(s1.__sizeof__()+s1.__dict__.__sizeof__())#120
print(s2.__sizeof__())#32 #PointSlots нет dict меньше памяти и на 30% быстрее выполняется



class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a, b) -> None:
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.height+self.width)*2

    @property
    def area(self):
        return self.height*self.width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

a=Rectangle(3,4)
a.area
a.perimetr


class Square(Rectangle):
    __slots__ = 'color'#subclass сохранил особенности slots
    #__slots__ = set()#ели нужно что бы subclass сохранил особенности slots но без новых данных
    
    def __init__(self, a, color) -> None:
        super().__init__(a, a)
        self.color = color


b=Square(5, 'red')
print(b)
