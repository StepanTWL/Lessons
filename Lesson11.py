with open('for_lesson11.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        print(a, b)

def f(a, b):
    return a * b

a = map(f, [1, 2, 3], [4, 5, 6])
print(list(a))#bez list budet adress ob'ekta

b = map(lambda x: x + 15, (2, 4, 5))
print(list(b))

def ff(c):
    if c % 2 == 0:
        return c

c = filter(ff, (2, 4, 5))
print(list(c))

d = filter(lambda x: (x % 2 == 0), (2, 4, 5))
print(list(d))

from asyncore import write
from functools import reduce
from random import random
from unittest import result
from xml.etree.ElementInclude import include

print(reduce(lambda a, b: a * b, (50, 57, 100, 20)))

e = [1, 2, 3, 4, 5]
f = 'abcde'
result = zip(e, f)#spisok iz kortejei
print(list(result))

#Задание:
#Создать текстовый файл (.txt) средствами вашей операционной системы, заполнить его любыми цифрами в 1 столбик. 
#Затем написать программу, в которой при помощи функции map считать все эти цифры в один список. 
#Затем, используя функцию filter, создать новый список, в котором останутся только нечетные цифры из предыдущего списка
import random

spisok = []
spisok1 = []
s = [str(random.randint(1000, 9999)) for i in range(1, 21)]
new_file = open("for_lesson11s.txt", "w+")
for i in s:
     new_file.write(i + '\n')
new_file.close()

with open("for_lesson11s.txt", "r") as f:
    for line in f:
        spisok.append([int(x) for x in line.split("\t")])
spisok = sum(spisok, [])

def f(a):
    if a % 2:
        return a
        
spisok1 = filter(f, spisok)
print(list(spisok1))
new_file.close()