a = {1, 2, 3, 1, 2, 3}
print(a)

b = set('wefwefwfsdfsfew')
print(b)

c = set([1,2,1,2,3,4,4,1])
d = set(range(10))
print(c)
print(d)

f = set()#pustoe mnojestvo

e = [1, 5, 3, 1, 2, 2, 0]
e = list(set(e))
print(e)

h = {0, 2, 8, 6, 8}
h.add(5)
h.update([5,2,-1,9])
h.update('hello')
h.update({-2, -3, -4})
print(h)

h.discard(0)
h.remove('e')#u dannogo metoda udaleniya oshibka budet esli takogo elementa net
h.pop()#udalyaet slu4ainyi element
print(h)
h.clear()
print(h)

t = {0, 2, 8, 6, 8}
r = {0, 1, 3, 9, 2}
print(len(t))
print(8 in t and 7 not in t)
print(t & r)
print(t.intersection(r))
t.intersection_update(r) #t&=r#izmenyaet spisok t
print(t)


t1 = {0, 2, 8, 6, 8}
r1 = {0, 1, 3, 9, 2}
print(t1 | r1)
print(t1.union(r1))
t1 = t1.union(r)
print(t1)


t2 = {0, 2, 8, 6, 8}
r2 = {0, 1, 3, 9, 2}
print(t2-r2)
print(r2-t2)
print(t2 ^ r2)
print(t2 == r2)
print(t2 < r2)
for i in t2:
    print(i)

text = input()
while text!='':
    print(text.split())

    text = input()

text = input()
k=set()
while text!='':
    slova = text.split()
    k.update(slova)
    print(k)

    text = input()