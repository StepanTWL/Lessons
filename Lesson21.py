#nahojdenie delitelei 4isla
from operator import le


n = int(input())
i = 1
a = []
while i**2 <= n:
    if n % i == 0:
        a.append(i)
        if i != n//i:
            a.append(n//i)
    i += 1
a.sort()
print(a)

j=1
while j<5:
    j += 1
    a=input()
    if a =='exit':
        break
    if len(a) <5:
        continue
    print(a, len(a))
else:
    print('lol')