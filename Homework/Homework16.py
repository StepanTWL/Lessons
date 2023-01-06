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


s = input()
arr = list(map(str, s.split()))
arr1 = list(map(str, s.lower().split()))
index = [0]*len(arr)
index[0] = 1
for i in range(1, len(arr)):
    if not arr[i].lower() in arr1[:i]:
        index[i] = 1
for i in range(len(arr)):
    if index[i]:
        print(arr[i], end=' ')


my_frozen = frozenset([int('7' * i) for i in range(1, 78)])

words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']
words_with_position = []
for i in range(len(words)):
    words_with_position.append((words[i], i+1))
print(words_with_position)



def count_AGTC(dna: str):
    A = 0
    G = 0
    T = 0
    C = 0
    if 'A' in dna:
        A = dna.count('A')
    if 'G' in dna:
        G = dna.count('G')
    if 'T' in dna:
        T = dna.count('T')
    if 'C' in dna:
        C = dna.count('C')
    print((A, G, T, C))


count_AGTC('AGGTC')

from typing import Union


def first_repeated_word(text: str) -> Union[str, None]:
    'Находит первый дубль в строке'
    arr = list(map(str, text.split()))
    for i in range(1, len(arr)):
        if arr[i] in arr[:i]:
            return arr[i]
    return None
print(first_repeated_word("ab ca bc ca ab bc"))



def check_sum(*args):
    summa = 0
    for i in args:
        summa += i
    if summa >= 50:
        print('verification passed')
    else:
        print('not enough')


check_sum(*list(map(int, input().split())))

from typing import Union, List


def create_actor(name: str = 'Райан', surname: str = 'Рейнольдс', age: int = 46, **kwargs):
    dictt = {}
    dictt['name'] = name
    dictt['surname'] = surname
    dictt['age'] = age
    for key, value in kwargs.items():
        dictt[key] = value
    return dictt


dictt1 = create_actor(name='Jack', age=20, x=(10, 20, 30), z=100)

sale_lambda = lambda x: x*0.9 if x > 50.0 else x


def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition(x: float, y: float):
        print(float(x + y))

    def subtraction(x: float, y: float):
        print(float(x - y))

    def division(x: float, y: float):
        if not y:
            print('На ноль делить нельзя!')
        print(x / y)

    def multiplication(x: float, y: float):
        print(float(x * y))

    if operation == 'a':
        addition(x, y)
    elif operation == 's':
        subtraction(x, y)
    elif operation == 'd':
        division(x, y)
    elif operation == 'm':
        multiplication(x, y)
    else:
        print('Ошибка. Данной операции не существует')

calculate(10, 4, 's')


arr = list(map(int, input().split()))

dictt = {}

if len(arr) == (0 or 1):
    print(dictt)
else:
    dictt[arr[-2]] = arr[-1]
    arr.pop(-1)
    arr.pop(-1)
    while len(arr):
        dictt = {arr[-1]: dictt}
        arr.pop(-1)
print(dictt)



def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, 'r') as file:
        for i in range(n):
            print(file.readline(), end='')


file_n_lines("hello.txt", 3)
"""

def find_lines_len_more_6(file_name:str) -> int:
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            if len(line) > 6 or (len(line) > 7 and line[-1] == '\n'):
                count += 1
    print(count)

find_lines_len_more_6('hello.txt')

pass
