#магические методы __eq__ (==), __ne__ (!=), __lt__ (<), __le__ (le), __gt__ (>), __ge__ (>=)


from traceback import print_tb


class Rectangle:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a*self.b

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Rectangle):
            return self.a == __o.a and self.b == __o.b

    def __ne__(self, __o: object) -> bool:
        if isinstance(__o, Rectangle):
            return self.a != __o.a or self.b != __o.b

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Rectangle):
            return self.area < __o.area
        elif isinstance(__o, (int, float)):
            return self.area < __o

    def __le__(self, __o: object) -> bool:
        return self == __o or self < __o


q = Rectangle(1, 2)
w = Rectangle(2, 1)

print(q == w)#false
print(q != w)#true
print(q > w)#false метод не определен но питон сам может поменять местами объекты и проверить уже w < q
print(q < w)#false
print(q <= w)#false
print(q >= w)#false