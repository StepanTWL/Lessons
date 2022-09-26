#магический метод __call__
from time import perf_counter
from typing import Any

class Counter:

    def __init__(self) -> None:
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f"наш экземпляр вызывался {self.counter} раз")

    def average(self):
        return self.summa / self.length


a=Counter()#init object <__main__.Counter object at 0x00000000039E09D0>
a()#object call <__main__.Counter object at 0x00000000039E09D0>
q=Counter()
q(1,2,3)#наш экземпляр вызывался 1 раз
print(q.counter)#1
print(q.summa)#6
print(q.length)#3
print(q.average())#2.0


class Timer:

    def __init__(self, func) -> None:
        self.fn = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start = perf_counter()
        result = self.fn(*args, **kwds)
        finish = perf_counter()
        print(f"функция отработала за {finish-start}")
        return result

@Timer
def fact(n):
    pr=1
    for i in range(1, n+1):
        pr *= i
    return pr

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fact(7))#функция отработала за 4.105300000001311e-05
              #5040

print(Timer(fib)(40))#такое же декорирование как и @Timer только исключает вложенные функции
                        #функция отработала за 0.026036191999999958
                        #6765