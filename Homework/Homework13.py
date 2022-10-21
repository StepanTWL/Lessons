"""
row,col = map(int, input().split())
arr=[[0]*col for i in range(row)]
count=1
for q in range(row*col):
    for i in range(row):
        for j in range(col):
            if i+j==q:
                arr[i][j]=count
                count+=1
for i in range(row):
    for j in range(col):
        print(str(arr[i][j]).ljust(3), end='')
    print()

row,col = map(int, input().split())
arr=[[0]*col for i in range(row)]
count=1
for i in range(row):
    if i%2:
        for j in range(col-1,-1,-1):
            arr[i][j]=count
            count+=1
    else:
        for j in range(col):
            arr[i][j]=count
            count+=1
for i in range(row):
    for j in range(col):
        print(str(arr[i][j]).ljust(3), end='')
    print()


row,col = map(int, input().split())
arr=[[0]*col for i in range(row)]
count=1
for i in range(row):
    for j in range(col):
        arr[i][j]=count
        if count==col:
            count=1
        else:
            count+=1
    if count==col:
        count=1
    else:
        count+=1
for i in range(row):
    for j in range(col):
        print(str(arr[i][j]).ljust(3), end='')
    print()

n = int(input())
arr=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i<=j and i<=n-1-j) or (i>=j and i>=n-1-j):
            arr[i][j]=1
for i in range(n):
    for j in range(n):
        print(str(arr[i][j]).ljust(3), end='')
    print()

n=int(input())
arr=[[0]*n for i in range(n)]
arr1=[i for i in range(1,n**2+1)]
sum=[0]*(2*n+2)
suc=0
for i in range(n):
    arr[i]=list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if not arr1.count(arr[i][j]):
            suc=1
        else:
            arr1.pop(arr1.index(arr[i][j]))
    if suc:
        break
if not suc:
    for i in range(n):
        sum[0]+=arr[i][i]
        sum[1]+=arr[n-1-i][i]
        for j in range(2,n+2):
            sum[j]+=arr[j-2][i]
            sum[j+n]+=arr[i][j-2]
    if min(sum)==max(sum):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

n=input()
arr=[['.']*8 for i in range(8)]
a=int(n[1])-1
b=ord(n[0])-97
arr[a][b]='N'
for i in range(8):
    for j in range(8):
        if (a-i)*(b-j) == 2 or (a-i)*(b-j) == -2:
            arr[i][j] = '*'
for i in range(7,-1,-1):
    print(*arr[i])

n=int(input())
arr=[[0]*n for i in range(n)]
arr1=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        arr1[j][n-1-i] = arr[i][j]
for i in range(n):
    print(*arr1[i])


n=int(input())
arr=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int, input().split()))
for i in range(n//2):
    for j in range(n):
        arr[i][j], arr[n-i-1][j] = arr[n-i-1][j], arr[i][j]
for i in range(n):
    print(*arr[i])


n=int(input())
arr=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int, input().split()))
sum=[0]*4
for i in range(n):
    for j in range(n):
        if (i<j and i<n-j-1):
            sum[0]+=arr[i][j]
        elif (i<j and i>n-j-1):
            sum[1]+=arr[i][j]
        elif (i>j and i>n-j-1):
            sum[2]+=arr[i][j]
        elif (i>j and i<n-j-1):
            sum[3]+=arr[i][j]
print(f"Верхняя четверть: {sum[0]}")
print(f"Правая четверть: {sum[1]}")
print(f"Нижняя четверть: {sum[2]}")
print(f"Левая четверть: {sum[3]}")


n=int(input())
arr=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int, input().split()))
maxx=arr[0][0]
for i in range(n):
    for j in range(n):
        if (i<=n//2 and (j <= i or j >= n-i-1)) or (i>n//2 and (n-j-1>=i or j>=i)):
            if maxx<arr[i][j]:
                maxx=arr[i][j]
print(maxx)


arr = list(map(list, input().split()))
n = int(input())
arr1=[]
while len(arr):
    for i in range(n):
        if not len(arr):
            break
        if i:
            arr1[-1].append(*arr.pop(0))
        else:
            arr1.append(arr.pop(0))
print(arr1)


row,col = map(int, input().split())
arr1=[]
arr2=[]
arr=[[0]*col for i in range(row)]
for i in range(row):
    arr1.append(list(map(int, input().split())))
input()
for i in range(row):
    arr2.append(list(map(int, input().split())))
for i in range(row):
    for j in range(col):
        arr[i][j] = arr1[i][j]+arr2[i][j]
for i in range(row):
    print(*arr[i])


row1,col1 = map(int, input().split())
arr1=[]
for i in range(row1):
    arr1.append(list(map(int, input().split())))
input()
row2,col2 = map(int, input().split())
arr2=[]
for i in range(row2):
    arr2.append(list(map(int, input().split())))

arr=[[0]*col2 for i in range(row1)]

for i in range(row1):
    for j in range(col2):
        sum=0
        for k in range(col1):
            sum += arr1[i][k]*arr2[k][j]
        arr[i][j]=sum
for i in range(row1):
    print(*arr[i])


import copy
arr=[]
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
m = int(input())

arr_tmp = copy.deepcopy(arr)
arr1=[[0]*n for i in range(n)]

for i in range(m-1):
    for j in range(n):
        for k in range(n):
            sum=0
            for l in range(n):
                sum += arr[j][l]*arr_tmp[l][k]
            arr1[j][k]=sum
    arr_tmp = copy.deepcopy(arr1)
for i in range(n):
    print(*arr_tmp[i])


import re

arr=list(map(str, (re.sub(r'[.,;:-?-!]', '', input())).lower().split()))
for i in range(len(arr)):
    if not arr[i][-1].isalpha():
        arr[i] = arr[i][:-1]
print(len(set(arr)))



arr=list(map(int, input().split()))
print('NO')
for i in range(1,len(arr)):
    if arr[i] in arr[:i]:
        print('YES')
    else:
        print('NO')


sett1=set(map(int, input().split()))
sett2=set(map(int, input().split()))
print(*(sorted(sett1 & sett2)))


n=int(input())
sett=set(input())
for i in range(1, n):
    sett = sett & set(input())
if len(sett):
    print(*sorted(sett))


sett1=set(input())
sett2=set(input())
if (sett1 & sett2):
    print('YES')
else:
    print('NO')



sett1=set(map(int, input().split()))
sett2=set(map(int, input().split()))
sett3=set(map(int, input().split()))
sett4=sorted(sett3 - (sett1 | sett2), reverse=True)
print(*sett4)


sett=set(range(11))
sett1=set(map(int, input().split()))
sett2=set(map(int, input().split()))
sett3=set(map(int, input().split()))
sett4=sorted(sett - (sett1 | sett2 | sett3))
print(*sett4)



words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
mywords = {c for c in words if c[0].islower()}
print(*sorted(mywords))


words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
mywords = {c.lower() for c in words}
print(*sorted(mywords))


import re
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
mywords = {c for c in (re.sub(r'[().,;:-?-!]', '', sentence)).lower().split() if len(c)<4}
print(*sorted(mywords))



files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myfiles = {c.lower() for c in files if c[-4::].lower() == '.png'}
print(*sorted(myfiles))
"""

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

my_dict = {}
for i in users:
    for j in i:
        if j