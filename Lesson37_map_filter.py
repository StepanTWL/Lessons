a = [-1,2,-3,4,-5]
b = list(map(abs, a))
print(b)#[1,2,3,4,5]

def f(x):
    return x**2

c = list(map(f,a))#1 4 9 16 25

d = ['abc', 'def', 'hig']
e = list(map(str.upper, d))#['ABC', 'DEF', 'HIG']
i = list(map(lambda x: x[::-1], d))#['cba', 'fed', 'gih']
g = list(map(list, d))#[['a', 'b', 'c'], ...] вложенный 
h = list(map(sorted, g))#[['a', 'b', 'c'], ...]

s = list(map(int, input().split()))


################# FILTER #################
#используюся функции которые возращают bool
def f2(x):
    return x > 10

k = [0, 52, 5, 59, 4, 0, 100]
l = list(filter(f2, k))# [52, 59, 100]
m = list(filter(bool, k))# [52, 5, 59, 4, 100]
m1 = list(filter(None, k))# [52, 5, 59, 4, 100]
n = ['world', 'hello', '123']
o = list(filter(lambda x: len(x)>4, n))#['world', 'hello']
p = 'asdf22f2faf423t34'
r = list(filter(str.isdigit, p))#['2','2',...]

t = {
    'moscow': 800,
    'boston': 750,
    'LA':900,
}
u = list(filter(lambda x: t[x] > 800, t))
print(u)

