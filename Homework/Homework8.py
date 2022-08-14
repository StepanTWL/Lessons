"""
S = int(input())
Petya = 0
Katya = 0
Sereja = 0
Petya = Sereja = int(S / 6)
Katya = int((Sereja + Petya) * 2)
print(Petya, Katya, Sereja)


s = list(map(int, input().split()))
sum = s[0]*3 + s[1]*5 + s[2]*12
print(sum)


s = list(map(int, input().split()))
print(sum(s)/len(s))


hour_start = int(input())
min_start = int(input())
sec_start = int(input())
hour_stop = int(input())
min_stop = int(input())
sec_stop = int(input())
n = 3600*hour_stop+60*min_stop+sec_stop - (3600*hour_start+60*min_start+sec_start)
print(n)


n, m = list(map(int, input().split()))
print((n+m-1)-n, (n+m-1)-m)


a1, a2 = list(map(float, input().split()))
if a1>a2:
    print(a1-a2)
else:
    print(a2-a1)


a, b, c = list(map(int, input().split()))
s = []
s.append(a+b+c)
s.append(a*b+c)
s.append(a+b*c)
s.append(a*b*c)
s.append(a*(b+c))
s.append((a+b)*c)
print(max(s))


s = float(input())
print(round(s, 2), round(s, 3))

s = list(map(str, input().split()))
print(','.join(s))


n = int(input())
print(str(n-1)+'<'+str(n)+'<'+str(n+1))


s1 = input()
s2 = input()
s3 = input()
print(s1+'---'+s2+'---'+s3)


s = input()
s1 = ''
for i in range(1,5):
    s1 += str(i)+s
print(s1+'5')


s = input()
print(s, end=' - Сказала она!')


print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')

n = int(input())
i = 0
while n>0:
    if n >= 100:
        i += n//100
        n -= 100*(n//100)
    elif n>=20:
        i += n//20
        n -= 20*(n//20)
    elif n>=10:
        i += n//10
        n -= 10*(n//10)
    elif n>=5:
        i += n//5
        n -= 5*(n//5)
    else:
        i += n
        n = 0
print(i)


num1, num2 = list(map(int, input().split()))
arr=list(map(int, input().split()))
arr+=list(map(int, input().split()))
arr1=[0]*max(arr)
arr2=[]
count=0
while count < num1+num2:
    arr1[arr[count]-1]+=1
    count += 1
for i in range(len(arr1)):
    while arr1[i]>0:
        arr2.append(i+1)
        arr1[i] -= 1
print(*arr2)


def pair(num:int, arr1:list, arr2:list) ->int:
    count=0
    for i in range(num):
        if arr2[arr1[i]-1] > 0:
            arr2[arr1[i]-1] -= 1
            count+=1
        elif arr2[arr1[i]] > 0:
            arr2[arr1[i]] -= 1
            count+=1
        elif arr2[arr1[i]+1] > 0:
            arr2[arr1[i]+1] -= 1
            count+=1
    return count
    
num1=int(input())#сортировка мальчиков и девочек для танцев
arr1=list(map(int, input().split()))
arr1.sort()
arr1_=[0]*100
num2=int(input())
arr2=list(map(int, input().split()))
arr2.sort()
arr2_=[0]*100
count=0
for i in arr1:
    arr1_[i]+=1
for i in arr2:
    arr2_[i]+=1
if num1 < num2:
    count = pair(num1, arr1, arr2_)
else:
    count = pair(num2, arr2, arr1_)
print(count)


n, m = list(map(int, input().split()))
arr=[]
maxx=[]
summ=[]
index=[]
ind=-1
for i in range(n):
    arr.append(list(map(int, input().split())))
    summ.append(sum(arr[i]))
    maxx.append(max(arr[i]))
tmp=max(maxx)
while maxx.count(tmp): 
    index.append(maxx.index(tmp))
    maxx[maxx.index(tmp)]=0
if len(index) > 1:
    maxxx=0
    for i in index:
        if summ[i] > maxxx:
            ind=i
            maxxx = summ[i]
elif len(index):
    ind=index[0]
print(ind)



n, m = list(map(int, input().split()))
arr=[]
maxx=[]
index=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
    maxx.append(max(arr[i]))
tmp=max(maxx)
while maxx.count(tmp): 
    index.append(maxx.index(tmp))
    maxx[maxx.index(tmp)]=0
print(len(index))

arr1=[]
arr2=[]
count=0
n,m=list(map(int, input().split()))
for i in range(n):
    arr1.append(input())
input()
for i in range(n):
    arr2.append(input())
for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            count+=1
print(count)


n, num=list(map(int, input().split()))
count=0
arr=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] = (i+1)*(j+1)
        if arr[i][j]==num:
            count+=1
print(count)


n, m=list(map(int, input().split()))
arr=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i%2:
            arr[i][-j-1]=j+i*m
        else:
            arr[i][j]=j+i*m
    print(*arr[i])



n=int(input())
i=0
x_last=0
y_last=0
arr=[[0]*n for i in range(n)]
way=0#0-left,1-down,2-right,3-top
while i < n**2 and arr[x_last][y_last] == 0:
    i += 1
    if way==0:
        if y_last<n-1:
            if arr[x_last][y_last+1] == 0:
                arr[x_last][y_last]=i
                y_last += 1
                continue
            else:
                arr[x_last][y_last]=i
                x_last += 1
                way = 1
                continue
        else:
            i-=1
            way = 1
            continue
    if way==1:
        if x_last<n-1:
            if arr[x_last+1][y_last] == 0:
                arr[x_last][y_last]=i
                x_last += 1
                continue
            else:
                arr[x_last][y_last]=i
                y_last -= 1
                way = 2
                continue
        else:
            i-=1
            way = 2
            continue
    if way==2:
        if y_last>0:
            if arr[x_last][y_last-1] == 0:
                arr[x_last][y_last]=i
                y_last -= 1
                continue
            else:
                arr[x_last][y_last]=i
                x_last -= 1
                way = 3
                continue
        else:
            i-=1
            way = 3
            continue
    if way==3:
        if x_last>0:
            if arr[x_last-1][y_last] == 0:
                arr[x_last][y_last]=i
                x_last -= 1
                continue
            else:
                arr[x_last][y_last]=i
                y_last += 1
                way = 0
                continue
        else:
            i-=1
            way = 0
            continue
for i in range(n):
    print(*arr[i])        


zeroes = [0]*100
print(zeroes)
n=int(input())
print([i for i in range(1,n+1)])
n=int(input())
print([i for i in range(1,n+1) if not n%i])
n=int(input())
print([i for i in range(n,n**2+1) if i%2])
n,m=list(map(int, input().split()))
if n <= m:
    print([i**2 for i in range(n, m+1)])
else:
    print([i**3 for i in range(n, m-1, -1)])
s='Create a list of the first letters of every word in this string'
arr=list(map(str, s.split()))
print([i[0:1] for i in arr])



from string import ascii_uppercase
n=int(input())
arr=ascii_uppercase[0:n]
print([i*(ord(i)-64) for i in arr]) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

from re import T


phrase = 'Take only the words that start with t in this sentence'
arr=list(map(str, phrase.split()))
print([i for i in arr if i[0].lower()=='t'])

lonely = 777,
print(type(lonely))

a=(1,)*3
b=tuple('R'*5)
c=tuple('A'*8)
d=(2,)*5
print(a+b+c+d)

n=int(input())
m=int(input())
arr=tuple(range(n,m+1))
print(arr)