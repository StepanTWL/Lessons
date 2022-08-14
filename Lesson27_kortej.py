#kortej(tuple)

a = (1, 5, 5, 6, 9)
b = 1, 5, 5, 6, 9
c = tuple(range(5))
d = ()
e = (1, 'dasds', 55 ,7, True)
print(1 in a)
print(a + b)
print(a*4)
print(min(a))
print(e.index(True),e.index(1))

b = list(b)
print(a.__sizeof__())#tuple zanimayut men'she mesta i  skoros' obrabotki bystree
print(b.__sizeof__())