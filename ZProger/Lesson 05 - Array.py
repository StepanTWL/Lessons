# Массивы экономит память, можно использовать для интерграции с с-подобными проектами, используется в многопроцессорности что бы создать share объекты (общие данные)
from array import array

a = array('i', [1, 2, 3])
print(a[-1])  # 3
print(a[1:])  # array('i', [2, 3])

if a.typecode == 'i':
    print('work')

b = array('i', [3, 2, 1])
print(a + b)  # array('i', [1, 2, 3, 3, 2, 1])
print(a * 2)  # array('i', [1, 2, 3, 1, 2, 3])
print(a.itemsize)  # 4 - размер одного элемента
print(a.count(2))  # 1
c = a.tolist()
print(c)  # [1, 2, 3] - list
print(a.index(2))  # 1
a.insert(1, 5)
print(a)  # array('i', [1, 5, 2, 3])
print(a.pop())  # 3
print(a)  # array('i', [1, 5, 2])
