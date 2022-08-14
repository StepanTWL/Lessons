#key:value
a = {'kiev': 44, 'lvov': 55}
b = dict(kiev=44, lvov=55)
c = [['kiev',44],['lvov',55]]
c = dict(c)
print(a, b, c)
d = dict.fromkeys(['kiev', 'lvov'], 44)
e = {}
print(d)
print(e)
print(d['kiev'])
d['odessa']=66
del d['lvov']
d.setdefault('harkov', 33)
print(d)
print('odessa' in d)
print(d.get('lvov', 'nononono'))
print(d.popitem())#udalyaet lyuboe zna4enie i vozras4aet ego
print(d.keys())
print(d.values())
print(d.items())#preobrazuet slovar' v kolekciyu

for key,value in d.items():
    print(key, value)

person={}
s = 'Ivanov Ivan Kiev STI 5 2 3 4 2 2 2'
s = s.split()
person['LastName'] = s[0]
person['FirstName'] = s[1]
person['City'] = s[2]
person['university'] = s[3]
person['makrs']=[]
for i in s[4:]:
    person['makrs'].append(int(i))

print(person)

for key in person:
    print(person[key])

str = input()
k={}
for i in str:
    if i.isalpha():
        k[i] = k.get(i,0) + 1
        #if i in k:
        #    k[i] +=1
        #else:
        #    k[i] = 1
for i in sorted(k):
    print(i, k[i])


words={}
while True:
    s = input()
    if s in words:
        print('Слово', s, 'переводится как', words[s])
    else:
        print('Введите перевод слова', s)
        words[s] = input()