#arr = [x for l in arr for x in l]
from datetime import datetime
"""
count = int(input())
kub = [int(i) for i in input().split()]
arr = [0]*max(kub)
s = ''
for i in kub:
    for j in range(i):
        arr[j] += 1
for i in range(len(kub)):
    kub[i] = 0
for i in arr:
    for j in range(count-i, len(kub)):
        kub[j] += 1
for i in kub:
    s +=str(i)+' '
print(s)


balls, friends = [int(i) for i in input().split()]
s = input().lower()
arr = [0]*26
error = 0
for i in s:
    arr[ord(i)-97] += 1
for i in arr:
    if (i > friends):
        error = 1
        break
if error == 1:
    print('NO')
else:
    print('YES')


name1=input().upper()
name2=input().upper()
litter=input().upper()
s = [0]*26
for i in name1:
    s[ord(i)-ord('A')] += 1
for i in name2:
    s[ord(i)-ord('A')] += 1
for i in litter:
    s[ord(i)-ord('A')] -= 1
if min(s) or max(s):
    print('NO')
else:
    print('YES')


count, end_point = [int(i) for i in input().split()]
arr = []
n = []
m = []
for i in range(count):
    arr.append([int(i) for i in input().split()])
for i in range(count):
    for j in range(arr[i][0], arr[i][1]+1):
        if not n.count(j):
            n.append(j)
for i in range(1, end_point+1):
    if not n.count(i):
        m.append(str(i))
print(len(m))       
print(' '.join(m))


size, number = [int(i) for i in input().split()]
n = 0
for i in range(size):
    for j in range(size):
        if (i+1)*(j+1) == number:
            n += 1
print(n)


n = int(input("n="))
start_time = datetime.now()
a = []
for i in range(n+1):
    a.append(i)
lst = []
i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)
print(datetime.now() - start_time)


import math
x = int(input("x="))+1
n = int(input("n="))
start_time = datetime.now()
lst = []
a = []
for i in range(x):
    a.append(i)
for i in range(2, x):
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, x, i):
            a[j] = 0
print(lst)
print(datetime.now() - start_time)


siza_table, number = [int(i) for i in input().split()]
start_time = datetime.now()
i = 1
count = 0
while  i**2 <= number:
    if number%i==0 and i <= siza_table and number//i <= siza_table:
        if i != number//i:
            count +=2
        else:
            count +=1
    i += 1
print(count)
print(datetime.now() - start_time)

a = 0
b = 0
count = 0
n, m = [int(i) for i in input().split()]
while a**2 <= n and a <= m:
    if n-a**2==(m-a)**0.5:
        count += 1
    a += 1
print(count) 


n, m = [int(i) for i in input().split()]
arr = []
for i in range(n):
    if i%2==0:
        arr.append('#'*m)
        continue
    else:
        if (i+1)%4==0:
            arr.append('#'+'.'*(m-1))
            continue
        else:
            arr.append('.'*(m-1)+'#')
            continue
for i in arr:
    print(i)


f=open("INPUT.TXT", "r")
count = int(f.readline())
arr = [int(i) for i in f.readline().split()]
f.close()
lst = []
x = -1
y = 0
sum = 0
for i in range(count):
    x = arr.index(max(arr[x+1:]))
    sum += (x+1-y)*arr[x]
    if x+1 >= count:
        break
    y = x+1
f=open("OUTPUT.TXT", "w")
f.write(str(sum))
f.close()



n = int(input())
arr = []
for i in range(2*n+1):
    arr.append([' ']*(4*n+1))
for i in range(2*n+1):
    for j in range(0,4*n+1,2):
        if j/2 <= n and i <= n:
            if i + j/2 - n >= 0:
                arr[i][j] = arr[i][4*n-j] = arr[2*n-i][j] = arr[2*n-i][4*n-j] = str(i + j//2 - n)
for i in arr:
    print(''.join(i).rstrip())
for i in arr:
    print(i) 
"""

n = int(input())
arr = []
for i in range(n):
    arr.append([j for j in input().split()])
for i in range(n):
    for j in range(n):
        if i + j + 1 < n:
            arr[i][j], arr[n-(j+1)][n-(i+1)] = arr[n-(j+1)][n-(i+1)], arr[i][j]
for i in arr:
    print(' '.join(i))