from itertools import count


a = [0,1,4,1,3,2,1,0,4,4,1,2,3]
count = [0]*5
for i in a:
    count[i] += 1
print(count)
for i in range(5):
    if count[i] > 0:
        print((str(i)+' ')*count[i], end='')
print()

s = 'jnlaaiv8rf0]h88gtHytg98y ytdl7HH65'
letter = [0]*26

for i in s.lower():
    if 'a'<=i<='z':
        # print(i, ord(i)-97)#kodirovka ascii a=97
        letter[ord(i)-ord('a')] += 1

for i in range(len(letter)):
    if letter[i] > 0:
        print(chr(i+ord('a'))+' - ', letter[i])

for i in range(1,10):
    for j in range(1,i+1):
        print(j,end='')
    print()

from string import printable
print(printable)

for b1 in printable:
    for b2 in printable:
            print(b1, b2)

k = 0
for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        rez = b1+b2+b3+b4+b5+b6
                        if rez[0] in 'tkv' and rez[-1] in 'tkv':
                            if rez.count('a')+rez.count('u')==2:
                                k += 1
print(k)