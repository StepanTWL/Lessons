import Lesson44_module as les
import Lesson44_module as les# Второй раз функции в Lesson44_module запускаться не будут
#Если нужно повторно запустить то делается через importlib.reload(Lesson44_module)
import pprint
import sys

les.say_hello('Kolya')
print(les.a)
print(les.math.pi)
pprint.pprint(sys.path)
pprint.pprint(sys.path.append('d:\\MyProject\\Python\\Shake'))
pprint.pprint(sys.path)#+d:\\MyProject\\Python\\Shake

print(__name__)#Lesson44_module

from importlib import reload
les.b = 'hi'
les.a = 2
print(les.b)#hi
print(les.a)#2
reload(les)
print(les.b)#hello
print(les.a)#1

from Lesson44_module import *
a = 2
print(a)#2
reload(les)
print(a)#2
