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