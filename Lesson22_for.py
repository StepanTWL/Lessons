print(list(range(10,0,-1)))
print(sum(range(10)))
print(len(range(10,0,-1)))

for i in range(4):
    print(i,end=' ')
print()

from random import randint
for i in range(5):
    a = randint(1, 100)
    print(a, end=' ')
print()

for i in range(1,10):
    print('*'*i)

a = [10, 5, 0, 55, 81]
for i in a:
    print(i, end=' ')
    input()
print()

#obhod po index - pri takom variante rabota ne s kopiei spiska a s samim spiskom
a = [10, 5, 0, 55, 81]
for i in range(len(a)):
    print(a[i], end=' ')
    a[i] += 2
print()
print(a)

s='hello'
for i in s:
    print(i)

vowels = 'aeiou'
s = 'hkugaectuciotukguiof78fxd'
for i in range(len(s)-1):
    if s[i] in vowels and s[i+1] in vowels:
        print(s[i], s[i+1])