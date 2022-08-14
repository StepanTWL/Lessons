"""
arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if arr[i][j]:
            print(abs(i-2)+abs(j-2))


n = int(input())
arr = []
sum = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            sum +=arr[i][j]
print(sum)


n, m = list(map(int, input().split()))
arr1 = []
arr2 = []
sumarr = [[0]*m for i in range(n)]
for i in range(n):
    arr1.append(list(map(int, input().split())))
input()
for i in range(n):
    arr2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        sumarr[i][j] = str(arr1[i][j]+arr2[i][j])
for i in sumarr:
    print(' '.join(i))


n = int(input())
arr = []
s = True
for i in range(n):
    arr.append(list(map(int, input().split())))
dig = [arr[i][j] for i in range(n) for j in range(n) if i+j==n-1]
for i in range(len(dig)):
    if not dig[i] == dig[n-i-1]:
        s = False
if s:
    print('yes')
else:
    print('no')


n, m = list(map(int, input().split()))
arr = []
max = 0
a, b = 0, 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if max < arr[i][j]:
            max, a, b = arr[i][j], i, j
print(max)
print(a, b)


n, m = list(map(int, input().split()))
arr = []
maxx = 0
summ = [0]*n
a = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        summ[i] +=(arr[i][j])
        if maxx < arr[i][j]:
            maxx = arr[i][j]
            a.clear()
            a.append(i)
        elif maxx == arr[i][j]:
            a.append(i)
if len(a) == 1:
    print(a[0])
else:
    print(summ.index(max(summ)))

n, m = list(map(int, input().split()))
arr1 = []
arr2 = []
error = 0
for i in range(n):
    arr1.append(input())
input()
for i in range(n):
    arr2.append(input())
for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            error += 1
print(error)


n = int(input())#a матч
arr = []
error = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(1,n-1):
        if i+j >= n:
            continue
        if arr[i][0] == arr[i+j][1]:
            error +=1
        if arr[i][1] == arr[i+j][0]:
            error +=1
print(error)


n, m = list(map(int, input().split()))#морской бой 2
arr = []
count = 0
arr.append(list(map(str,'.'*(m+2))))
for i in range(n):
    arr.append(list(map(str, '.'+input()+'.')))
arr.append(list(map(str,'.'*(m+2))))
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i+1][j]=='.' and arr[i-1][j]=='.' and arr[i][j+1]=='.' and arr[i][j-1]=='.':
            count += 1
print(count)


n, m = list(map(int, input().split()))#торминатор
arr = []
arr1 = [[0]*m for i in range(n)]
for i in range(n):
    arr.append(list(map(str, input())))
for i in range(n):
    count = 0
    for j in range(m):
        if arr[i][j] == 'S':
            count = 1
    if count == 0:
        for k in range(m):
            arr1[i][k]=1
for i in range(m):
    count = 0
    for j in range(n):
        if arr[j][i] == 'S':
            count = 1
    if count == 0:
        for k in range(n):
            arr1[k][i]=1        
count = 0
for i in range(n):
    for j in range(m):
        if arr1[i][j] == 1:
            count +=1
print(count)


n, m = list(map(int, input().split()))#Художник
number = int(input())
coord = []
count = 0
arr = [[0]*m for i in range(n)]
for i in range(number):
    coord.append(list(map(int, input().split())))
for i in range(number):
    for j in range(coord[i][0], coord[i][2]):
        for k in range(coord[i][1], coord[i][3]):
            if arr[k][j] == 0:
                count += 1
            arr[k][j]=1
print(n*m-count)


count = 0#Симпатичный узор
arr = []
for i in range(4):
    arr.append(list(map(str, input())))
for i in range(3):
    for j in range(3):
        if arr[i][j]=='B' and arr[i+1][j]=='B' and arr[i][j+1]=='B' and arr[i+1][j+1]=='B':
            count = 1
        if arr[i][j]=='W' and arr[i+1][j]=='W' and arr[i][j+1]=='W' and arr[i+1][j+1]=='W':
            count = 1
if count:
    print('No')
else:
    print('Yes')
"""
