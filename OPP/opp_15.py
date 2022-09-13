#магические методы __bool__

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __len__(self):#если нет __bool__ то класс смотрит на __len__ когда используется bool(), если и __len__ нет то у класса bool() всегда true 
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


p1=Point(0,0)
p2=Point(1,0)
print(bool(p1))#falce
print(bool(p2))#true
    

    