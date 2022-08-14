"""
while True:
    s=input()
    if s[0] != 'я' and s[0] != 'Я':
        break

level = 0
cub_level = 0
sum = 0
n=int(input())
while sum<n:
    level += 1
    cub_level += level
    sum += cub_level
if sum==n:
    print(level)
else:
    print(level-1)

sum = 0
mul = 1
n = int(input())
while n>0:
    sum += n%10
    mul *= n%10
    n=n//10
print(mul-sum)

n, m = [int(i) for i in input().split()]
while n>0 and m>0:
    if (n%10 + m%10) > 9:
        print('No')
        break 
    n //= 10
    m //= 10
if (n%10 + m%10) == 0:
    print('Yes')

i = 0
sum = 0
n = int(input())
while n>0:
    if n%2 != 0:
        n -= 1
        i += 1
    n //= 2
print(i)


f = open("INPUT.TXT", "r")
a, b = [int(i) for i in f.readline().split()]
f.close()
while a!=b:
    if a > b:
        a = a-b
    else:
        b = b-a
f = open("OUTPUT.TXT", "w")
f.write(str(a))
f.close()


f = open("INPUT.TXT", "r")
a, b = [int(i) for i in f.readline().split()]
f.close()
while b>0:
    a, b = b, a%b
f = open("OUTPUT.TXT", "w")
f.write(str(a))
f.close()


f = open("INPUT.TXT", "r")
a, b = [int(x) for x in f.readline().split()]
mul = a*b
f.close()
while b>0:
    a, b = b, a%b
f = open("OUTPUT.TXT", "w")
f.write(str(mul//a))
f.close()


f = open("INPUT.TXT", "r")
n, m = [int(x) for x in f.readline().split()]
i = 1
f.close()
while m*i%n>0:
    i += 1
f = open("OUTPUT.TXT", "w")
f.write(str(i))
f.close()


f = open("INPUT.TXT", "r")
semen, nesemen, kucha = [int(x) for x in f.readline().split()]
f.close()
player = 0
while kucha>=0:
    if player==0:
        a, b = semen, kucha
        while b>0:
            a, b = b, a%b
        kucha -=a
        player = 1
    else:
        a, b = nesemen, kucha
        while b>0:
            a, b = b, a%b
        kucha -=a
        player = 0
f = open("OUTPUT.TXT", "w")
f.write(str(player))
f.close()


n, x = [int(x) for x in input().split()]
arr=[]
count = 0
for i in range(n):
    arr.append([0]*n)
for i in range(n):
    for j in range(n):
        arr[i][j] = (i+1)*(j+1)
for i in arr:
    print(i)
while n>0:
    n -= 1
    for i in arr[n]:
        if i == x:
            count += 1
print(count)


price, value = [int(x) for x in input().split()]
count = 0
while True:
    count += 1
    if (price*count - value) % 10 == 0 or price*count % 10 == 0:
        break
print(count)


f=open("INPUT.TXT", "r")
count = int(f.readline())
s = []
win = 0
for i in range(count):
    s.append([0]*2)
    s[i] = [int(x) for x in f.readline().split()]
    if (s[i][0] > s[i][1]):
        win += 1
    elif (s[i][0] < s[i][1]):
        win -=1
f.close()
f=open("OUTPUT.TXT", "w")
if win > 0:
    f.write("Mishka")
elif win < 0:
    f.write("Chris")
else:
    f.write("Friendship is magic!^^")
f.close()
"""

count = int(input())
s = []
win = 0
for i in range(count):
    s.append([0]*2)
    s[i] = [int(x) for x in input().split()]
    if (s[i][0] > s[i][1]):
        win += 1
    elif (s[i][0] < s[i][1]):
        win -=1
if win > 0:
    print("Mishka")
elif win < 0:
    print("Chris")
else:
    print("Friendship is magic!^^")



