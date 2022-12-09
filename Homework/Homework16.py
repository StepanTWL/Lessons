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


s=input().lower()
if s[:3] == 'mam':
    print('True')
else:
    print('False')



s=input().lower()
s1=input().lower()
if s[-len(s1):] == s1:
    print("True")
else:
    print("False")



s=input()
s1=input()
s2=input()
if s[-len(s2):] == s2 and s[:len(s1)] == s1:
    print("True")
else:
    print("False")


r=int(input())
g=int(input())
b=int(input())

s='#'+hex(r)[2:].zfill(2).up+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2)



my_list = [['q', 'w', 't'] for _ in range(15)]
my_list = ['q', 'w', 't']*15

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)

my_list = list(map(int, input().split()))
if 3 in my_list:
    my_list.remove(3)
if 5 in my_list:
    my_list.remove(5)
if 7 in my_list:
    my_list.remove(7)
if 9 in my_list:
    my_list.remove(9)
print(my_list)
"""

s=list(map(str, input().split()))


pass