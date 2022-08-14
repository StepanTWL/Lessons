a = [11,23,38,42]
#print(list(enumerate(a)))

for index,value in enumerate(a,10):
    print(index)
    print(value)


r = lambda x: x**2
h = lambda : 'hello'
t = lambda x: 'positive' if x>0 else 'negative'

print(r(7))
print(h())
print(t(3))
a.sort(key=lambda x: x%10)
print(a)

def linear(k,b):
    return lambda x: k*x+b

graf1 = linear(2,5)
print(graf1(3))

graf2 = linear(-4,1)
print(graf2(5))

a = [i**2 for i in range(10)]
print(a)

b = [i*5 for i in 'hello']
print(b)

import random
c = [random.randint(-10,10) for i in range(10)]
print(c)
d = [abs(i) for i in c]
print(d)
e = [i for i in c if i%2 == 0 and i%3==0]
print(e)
f = input().split()
f = [int(i) for i in f]
print(f)

n = 5
m = 4
g = [[0]*m for i in range(n)]
for i in g:
    print(i)

h = [(i,j) for i in 'abc' for j in [1, 2, 3]]
print(h)

k = [i*j for i in [4,5,6,7] for j in [1, 2, 3] if i*j>10]
print(k)