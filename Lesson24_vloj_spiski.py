a = [[0,2,4,6], [1,5,9,13], [3,10,17,19]]
b = ['hello', 'hi', 'world']
print(len(a))
print(a[2][3])
print(b[0][0])

for i in b:
    print(i)

for i in a:
    for j in i:
        print(j, end=' ')
    print()

for i in range(3):
    for j in range(4):
        a[i][j] += 10
        print(a[i][j],end=' ')
    print()
print(a)

for i in range(3):
    sum = 0
    for j in range(4):
        sum += a[i][j]
    print(sum)


a1=[]
n1=int(input())

for i in range(n1):
    a1.append([0]*n1)

for i in range(n1):
    for j in range(n1):
        if i==j:
            a1[i][j]=1
        elif i>j:
            a1[i][j]=2
        else:
            a1[i][j]=3

for i in a1:
    print(i)

triangle=[]
n2=int(input())

for i in range(n2+1):
    triangle.append([1]+[0]*n2)

for i in range(1, n2+1):
    for j in range(1, i+1):
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

for i in range(0, n2+1):
    for j in range(0, i+1):
        print(triangle[i][j], end=' ')
    print()


a=[]
n=int(input())
m=int(input())

for i in range(n):
    b=[]
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)