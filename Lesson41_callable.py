#1 Встроенные функции
len('hello')
callable(len)#проверка вызываемости функции - True
int('43')#43

#2 Встроенные методы объекты
a=[1,2,3]
a.sort()

#3 Самописные функции
def f(x):
    return x*2

#4 Классы
class Cat:
    pass
bob = Cat()
callable(bob)#false

#5 Экземпляры классов
class Cat1:
    def __call__(self, *args, **kwds):
        print('123')
bob1 = Cat1()
print(callable(bob1))#true

#6 Методы классов
class Cat2:
    def __call__(self, *args, **kwds):
        print('123')
    def say_hello(self):
        print('hello')

bob2 = Cat2()
print(callable(bob2.say_hello))#true

#7 Функции-генераторы
def f1():
    n = 0
    while True:
        yield n
        n += 1
callable(f1)#true