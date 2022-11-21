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
"""