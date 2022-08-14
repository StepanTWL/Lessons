import random


a = [0 for i in range(10)]#[0 ... 0]
b = [i for i in range(10)]#[0 ... 9]
c = [i**2 for i in range(10)]#[0 ... 81]
d = [i*5 for i in 'hello']#['hhhhh' ... 'ooooo']
e = [random.randint(-10,10) for i in range(10)]
f = [abs(i) for i in e]
g = [i for i in f if i%2==0]
y, z = 3, 3
h = [[0]*y for i in range(z)]#[[0,0,0],[0,0,0],[0,0,0]]
k = [(i,j) for i in 'abc' for j in [1,2,3]]#[('a',1), ..., ('c',3)]
l = [i*j for i in [1,2,3] for j in [1,2,3] if i*j>5]#[6,6,9]
print(a, b, c, d, f, g, h, k, l)


m = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Efremov', 2006),
]
n = [i[0] for i in m]
o = [i[0] for i in m if i[0].startswith('E')]
p = [i[0][0] for i in m if i[1]>2000]
q = {
    'Sidorov': {'age':1995, 'hobby':'soccer', 'car': 'BMW'},
    'Lukov': {'age':2002, 'hobby':'basketball', 'car': 'Opel'},
    'Petrov': {'age':1991, 'hobby':'chess', 'car': 'Audi'},
    'Efremov': {'age':2006, 'hobby':'tennis', 'car': 'Fiat'},
}
r = [q[i] for i in q]#[{'age':1995, ...}...]
s = [(i,q[i]['car']) for i in q if q[i]['age']<2000 and q[i]['hobby']=='soccer']#[('Sidorov', 'BMW'), ('Efremov', 'Audi')]
print(n, o, p, r, s)

t = 'iihu88yyftufuyf8678d6sr80u99u-0y97rf56s64a4688ghy'
u = [int(i) for i in t if i.isdigit()]
print(u)

v = [[random.randint(1, 6) for j in range(y)] for i  in range(z)]
for i in v:
    print(i)
w = [v[i][j] for i in range(y) for j in range(z) if i==j]#значения диаганали
y = [v[i][1] for i in range(y)]#столбец 2
print(w, y)