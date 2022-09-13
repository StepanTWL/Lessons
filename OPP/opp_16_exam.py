from opp_16 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_area(), rect2.get_area())

sq1 = Square(3)
sq2 = Square(12)
print(sq1.get_area(), sq2.get_area())

crl1 = Circle(3)
crl2 = Circle(12)

figures = [rect1, rect2, sq1, sq2, crl1, crl2]
for fig in figures:
    print(fig, fig.get_area())

"""
Rectangle 3x4 12
Rectangle 12x5 60
Square 3x3 9
Square 12x12 144
Circle raduis=3 28.26
Circle raduis=12 452.16
"""