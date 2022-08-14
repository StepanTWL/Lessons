#zip -> iterator
a = [5, 6, 7, 8]
b = [100, 200, 300, 400]

rez = zip(a, b)
print(list(rez))#[(5, 100), ..., (8, 400)]

c = [5, 6, 7]
d = [100, 200, 300, 400]
e = 'abcd'

rez1 = zip(c, d)
print(list(rez1))#[(5, 100), ..., (7, 300)]
# т.к. rez итератор то его можно обходить 1 раз, можно єто избежать обернув в list()

rez1 = zip(c, d, e)#[(5, 100, 'a'), ..., (8, 400, 'd')]

for t1, t2, t3 in zip(c,d,e):
    print(t1, t2, t3)#5 100 a \n 6 200 b...

col1,col2,col3 = zip(*rez1)
print(col1,col2,col3)#(5,6,7,8) (100,200,300,400) ('a', 'b', 'c', 'd')


#sort - метод списка; sorted - встроенная функция
k = [4, -10, 2, 0, 999]
l = 'hello world'
m = ('hi', 'zero', 'null')
k.sort()
l
k = sorted(k)#[-10, 0, 2, 4, 999]
k = sorted(k, reverse=True)#[999, 4, 2, 0, -10]
l = sorted(l)#[' ', 'd'...]
m = sorted(m)#['hi', 'null', 'zero']


def f(x):
    return x%10, x//10%10 #сортировка по двум параметрам (сначала отсортирует по 1 потом по 2 признаку)

a1 = [4, -10, 43, -300, 54, 289]
a1 = sorted(a1, key=abs)#[4, -10, 43, 54, 289, -300]

b1 = ['aaa', 'ZZZ', 'eee', 'BBB']
b1 = sorted(b1, key=str.lower)#['aaa', 'BBB', 'eee', 'ZZZ']

c1 = ['aaa 43', 'ZZZ 80', 'eee 22', 'BBB 11']
c1 = sorted(c1, key=lambda x: int(x.split()[1]))#['BBB 11', 'eee 22', 'aaa 43', 'ZZZ 80']

d1 = ['aaa 1', 'ZZZ 2', 'eee 1', 'BBB 2']
d1 = sorted(d1, key=lambda x: (int(x.split()[1]), x.split()[0].lower()))#['aaa 1', 'eee 1', 'BBB 2', 'ZZZ 2']
d1 = sorted(d1, key=lambda x: (-int(x.split()[1]), x.split()[0].lower()))#['BBB 2', 'ZZZ 2', 'aaa 2', 'eee 2']
d1 = sorted(d1, key=lambda x: (int(x.split()[1]), x.split()[0].lower()), reverse=True)#['ZZZ 2', 'BBB 2', 'eee 1', 'aaa 1']
d1 = sorted(d1, key=lambda x: (x.split()[0].lower(), int(x.split()[1])))#['aaa 1', 'BBB 2', 'eee 1', 'ZZZ 2']
d1 = sorted(d1, key=lambda x: int(x.split()[1]))
d1 = sorted(d1, key=lambda x: x.split()[0].lower(), reverse=True)#['eee 1', 'aaa 1', 'ZZZ 2', 'BBB 2']