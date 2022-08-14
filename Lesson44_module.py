#Модуль отдельный файл *.py
a = 1
b = 'Hello'
import pprint
import calendar
import math
c = calendar.TextCalendar()
print(c.formatmonth(2022, 7))#календарь на 07.2022
pprint.pprint(locals())#информация о проекте
pprint.pprint(dir(math))#информация о методах в math

#import math as m
#print(m.pi)#3.14

#from math import pi, e
#print(pi)#3.14

#from math import *
#print(e)#2.71

def say_hello(name):
    print(f'hello {name}')

print(__name__)#__main___