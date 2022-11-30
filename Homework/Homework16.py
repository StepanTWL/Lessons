"""
from fractions import Fraction
from math import gcd

arr = []
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j and gcd(i, j) == 1:
            a = Fraction(i, j)
            arr.append(a)
sorted(arr)
for i in arr:
    print(i)


a = complex(input())
b = complex(input())

print(f'({a}) + ({b}) = ({a+b})')
print(f'({a}) - ({b}) = ({a-b})')
print(f'({a}) * ({b}) = ({a*b})')


numbers = [3+4j, 3+1j, -7+3j]
print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))


n = int(input())
z1 = complex(input())
z2 = complex(input())

print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1))


import time
import turtle


def square(side):
    turtle.speed(1)
    for i in range(8):
        turtle.left(45)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)


square(50)
time.sleep(500)



def greet(name, *args):
    s = 'Hello, '+name
    if not len(args):
        return (s + '!')
    s += ' and '
    for i in args:
        s += i + ' and '
    s = s[:-5] + '!'
    return s


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))



def print_products(*args):
    count = 1
    if not len(args):
        print('Нет продуктов')
        return
    for i in args:
        if isinstance(i, str) and not i=='':
            print(f'{count}) {i}')
            count += 1
    if count == 1:
        print('Нет продуктов')
        return

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')



def info_kwargs(**kwargs):
    for i in sorted(kwargs):
        print(f'{i}: {kwargs[i]}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


def comparator(args):
    if len(args):
        return sum(args)/len(args)
    return 0

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
print(min(numbers, key=comparator))
print(max(numbers, key=comparator))


def comparator(point):
    return point[0]**2+point[1]**2

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
print(sorted(points, key=comparator))



def comparator(data):
    return min(data)+max(data)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
print(sorted(numbers, key=comparator))
"""

input().startswith('mam')



"""
def comparator_i(i):
    def comparator(pair):
        return pair[n-1]
    return comparator

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

command = int(input())-1
[print(*t) for t in sorted(athletes, key=comparator_i[n])]
"""
