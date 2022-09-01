from math import sqrt
from msilib.schema import Class


class Cat:

    def __init__(self, name, breed='pers', age=1, color='white') -> None:
        print('hello')
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


bob = Cat('Bob')#hello
#breed: pers, name: Bob, age: 1, color: white
tom = Cat('Tom', 'siam', 15, 'black')




class Point:

    list_points = []

    def __init__(self, coord_x: int = 0, coord_y: int = 0) -> None:
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)
    
    def move_to(self, new_x: int, new_y: int) -> None:
        self.x = new_x
        self.y = new_y

    def go_home(self) -> None:
        self.move_to(0, 0)

    def print_point(self) -> None:
        print(f"Точка с координатами ({self.x}, {self.y})")

    def calc_distance(self, another_point) -> float:
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу точка')
        
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


p = Point()#0:0
p.move_to(4,5)#4:5
p.go_home()#0:0
p.print_point()#Точка с координатами (0, 0)
p.move_to(4,3)
p1 = Point()
print(p.calc_distance(p1))#5.0
print(Point.list_points[0].x)#p.x=4

