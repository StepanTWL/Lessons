#магические методы __eq__ (==), __hash__ 
#hash подерживается для неизменяемых объектов:int, string, float, tuple

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:#при определении этой функции перестает работать функция hash и ее тоже нужно переопределять
        return isinstance(__o, Point) and self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

p1=Point(1,2)
p2=Point(1,2)
print(p1==p2)
print(hash(p1))#-3550055125485641917
r={}
r[p1] = 100
print(r)#{<__main__.Point object at 0x00000000039CD910>: 100}


