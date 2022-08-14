from collections import Counter

l = 'asdfasdf'
w = ['qwe', 'zxc', 'asd', 'qwe', 'zxc']
letters = Counter(l)
print(letters)#Counter({'a': 2, 's': 2, 'd': 2, 'f': 2})
words = Counter(w)
print(letters)#Counter({'qwe': 2, 'zxc': 2, 'asd': 1})

for i in words.elements():
    print(i)#qwe\nzxc\n...

print(words.most_common())#[('qwe', 2), ('zxc', 2), ('asd', 1)] первые которые чаще появляются, можно в () указать сколько элементов (пар) выдать

letters['z']#0 а не как в словаре ошибка
r = Counter()
for i in [1,1,1,2,2,3]:
    r[i] += 1
print(r)#Counter({1: 3, 2: 2, 3: 1})
d = Counter([2,2,2,3,3,4])
print(r+d)#Counter({2: 5, 1: 3, 3: 3, 4: 1}) - взял все ключи с d i r и сложил их значения, можно и вычитать ключи у которых получается отрицательное значение не выводятся
t = Counter()
t[1] += 5
t[(1,2,3)] += 10
print(t)#Counter({(1, 2, 3): 10, 1: 5}) можно использовать tuple так как он изменяемый


from collections import defaultdict

s = defaultdict(int)
print(s)#defaultdict(<class 'int'>, {})
s['r']
print(s)#defaultdict(<class 'int'>, {'r': 0})
b=defaultdict(list)
print(b)#defaultdict(<class 'list'>, {})
b[1]
print(b)#defaultdict(<class 'list'>, {1: []})
b['a'] = 123
print(b)#defaultdict(<class 'list'>, {1: [], 'a': 123})
b.default_factory = lambda: [1,2,3]#по умолчанию
print(b[4])#[1,2,3]
print(b)#defaultdict(<function <lambda> at 0x00000000039D5670>, {1: [], 'a': 123, 4: [1, 2, 3]})
print(b[5])#[1,2,3]
print(b)#defaultdict(<function <lambda> at 0x00000000039D5670>, {1: [], 'a': 123, 4: [1, 2, 3], 5: [1, 2, 3]})

data = [
    ('ivanov1', 5),
    ('ivanov2', 2),
    ('ivanov1', 1),
    ('ivanov2', 8),
    ('ivanov2', 3),
    ('ivanov2', 3),
]
marks = defaultdict(int)
marks_list = defaultdict(list)
marks_uniq = defaultdict(set)
for surname, mark in data:
    marks[surname] += mark
    marks_list[surname].append(mark)
    marks_uniq[surname].add(mark)
print(marks)#defaultdict(<class 'int'>, {'ivanov1': 6, 'ivanov2': 16})
print(marks_list)#defaultdict(<class 'list'>, {'ivanov1': [5, 1], 'ivanov2': [2, 8, 3, 3]})
print(marks_uniq)#defaultdict(<class 'set'>, {'ivanov1': {1, 5}, 'ivanov2': {8, 2, 3}})


from collections import namedtuple#обращение в картеже не по индексам а по названиям 
human = namedtuple('Person', 'name surname date country')#создание класса с названием Person и атрибутами name surname date country
z = human('Joseph', 'Bauer', '1980-05-19', 'Canada')#z будет кортежом
print(z)#Person(name='Joseph', surname='Bauer', date='1980-05-19', country='Canada')
print(z._asdict())#{'name': 'Joseph', 'surname': 'Bauer', 'date': '1980-05-19', 'country': 'Canada'} делает словарь
print(z._replace(name='Ivan'))#Person(name='Ivan', surname='Bauer', date='1980-05-19', country='Canada') в отличии от tuple здесь можно изменять значения

from typing import NamedTuple
class Person_(NamedTuple):
    name: str
    surname: str
    data: str
    country: str

Person_('Joseph', 'Bauer', '1980-05-19', 'Canada')
