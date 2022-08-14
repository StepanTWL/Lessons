import numbers
from time import perf_counter
from tracemalloc import start


g = 'gray'
def colors(param='r'):
    y = 'yellow'
    g = 'green'
    def print_red():
        nonlocal y
        r = 'red'
        g = 'gray-green'
        print(r, y, g)#gray-green
        y = 'light-yellow'

    def print_blue():
        b = 'blue'
        g = 'gray-green'
        print(b, y, g)#blue light-yellow gray-green

    if param=='r':
        print_red()
    elif param=='b':    
        print_blue()
    else:
        print("i don't know this color")

colors()

#####################ЗАМЫКАНИЕ####################
def main_func(value):
    name = value
    def inner_func():
        print('hello', name)#замыкание - вложеная функция использует переменные из другой облости видимости
    return inner_func

b = main_func('Misha')
b()#hello Misha


def adder(value):
    def inner(a):
        return value+a
    return inner

a2 = adder(2)
print(a2(5))#2+5=7


def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
print(q())#1
print(q())#2
r = counter()
print(r())#1
print(r())#2

def averade_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return inner

r1 = averade_numbers()
print(r1(5))#5.0
print(r1(10))#7.5
q1 = averade_numbers()
print(q1(1))#1.0
print(q1(5))#3.0


#from datetime import datetime
from time import perf_counter
def timer():
    #start = datetime.now()
    start = perf_counter()
    def inner():
        #return datetime.now()-start
        return perf_counter()-start
    return inner

r2 = timer()
print(r2())
print(r2())


def add(a, b):
    return a+b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"функция {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)
    return inner

q = counter(add)
print(q(1, 2))#функция add вызывалась 1 раз
#3
print(q(2, 2))#функция add вызывалась 2 раз
#4

#декораторы нужны что бы дать функции новые возможности
def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, **kwargs)
        print('finish decorator...')

    return inner

def say():
    print('hello')

def buy(name):
    print('buy', name)

q = decorator(say)
q()#start decorator...\n hello\n finish decorator...
say = decorator(say)
say()#start decorator...\n hello\n finish decorator...

buy = decorator(buy)
buy('Vasya')#start decorator...\n buy Vasya\n finish decorator...


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

def header(func):
    def inner(*args, **kwargs):
        print('<t1>')
        func(*args, **kwargs)
        print('</t1>')
    return inner

s = table(header(buy))
s('Vasya')
#<table>
#<t1>
#start decorator...
#buy Vasya
#finish decorator...
#</t1>
#</table>

@table
@header
def buy1(name):
    print('buy', name)

buy1("vasya")
#<table>
#<t1>
#buy vasya
#</t1>
#</table>

#У декорируемых функций теряется название (__name__) и описание (__doc__)
#Можно решить эту проблему переопределением в декораторе перед return inner
#inner.__name__ = func.__name__
#inner.__doc__ = func.__doc__
#или функцией wraps (from functools import wraps) перед функцией inner
#@wraps(func)