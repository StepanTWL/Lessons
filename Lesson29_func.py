if False:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()


import turtle
def drawSquare(a, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()

"""
turtle.speed(1)
drawSquare(5, 'red')
turtle.goto(20, 20)
drawSquare(10, 'green')
"""
def square(x):
    return x**2

def factorial(x):
    pr = 1
    for i in range(2, x+1):
        pr *= i
    return pr

def sochet(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(sochet(2,1))

def sqAndPer(a, b):
    return a*b, (a+b)*2
square, perimetr = sqAndPer(2,3)
print(square, perimetr)

def s():
    global a 
    a = 30
    b = 10
    def q():
        nonlocal b
        b = 20
    q()
    print(b)

a = 20
s()
print(a)

#a - peredacha sylki an peremennuyu, a[:] - peredacha kopii/sreza

a, b, *c = [1, 2, 3, 4, 5, True]
print(a, b, c)
s = [1,5]
print(list(range(*s)))

def f(a,b,c,d):
    print(a,b,c,d)

a = ('hello', True, 20, [1, 2, 3])
f(*a)

def f(*args):
    print(args)
f(1,2,3,4,True,[1,2,3])

def sum1(*args):
    s=0
    for i in args:
        s+=i
    return s

print(sum1(1,2,3,4,5,6))

def slov(**kwargs):
    print(kwargs)
    for i, j in kwargs.items():
        print(i,j)

slov(kiev=44,lvov=55)

def outPrint(*args, sep='#',end='@'):
    print(args, sep, end)

outPrint(1,2,3,4,sep=90)
a = [1,2,3]
print(*a)

def append_to_list(value, my_list=None):#Нужно для того что бы my_list был разный при каждом вызове функции, если my_list=[] то без указания списка будет один раз создан пустой список и потом в него будет добавляться число при каждом вызове 
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))

def append_to_dict(key, value, my_dict=None):#Нужно для того что бы my_list был разный при каждом вызове функции, если my_list=[] то без указания списка будет один раз создан пустой список и потом в него будет добавляться число при каждом вызове 
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    print(my_dict, id(my_dict))

append_to_list(77)
append_to_list(99)
append_to_dict(7, 77)
append_to_dict(9, 99)

