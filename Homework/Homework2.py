"""
from math import ceil
i = 1
s = []
summ = 0
while True:
    print("Введите количество детей в классе №", i)
    t = input()
    if t == '':
        break
    if not t.isdigit():
        print("Введено не число")
        continue; 
    i += 1
    s.append(int(t))
for i in s:
    summ += ceil(i/2)
print("Количесто парт для", len(s), "классов - ", summ)


print((input())[3:5])


print(len(input().split()))


print(input().replace('@',''))


s = input()
arr = []
str = 'hello'
arr.append(s.find('h'))
if (arr[0] != -1):
    arr.append(s.find('e', arr[0]+1))
    if (arr[1] != -1):
        arr.append(s.find('l', arr[1]+1))
        if (arr[2] != -1):
            arr.append(s.find('l', arr[2]+1))
            if (arr[3] != -1):
                arr.append(s.find('o', arr[3]+1))
                if (arr[4] != -1):
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')


str = input()
a, b = str.find('f'), str.rfind('f')
if a == -1 and b == -1:
    print('В строке нет буквы f')
elif a == -1 and b != -1:
    print(b)
elif a != -1 and b == -1:
    print(a)
else:
    print(a,b)

str = input()
s = str.split()
print(s[1]+' '+s[0])

s = input()
str = 'WUB'
s1 = ''
s = s.split(str)
for i in s:
    if i != '':
        s1 += i + ' '
print(s1)


s1 = int(input())
s2 = [int(i) for i in input().split()]
s3 = [int(i) for i in input().split()]
s4 = [int(i) for i in input().split()]
s2 = sorted(s2)
s3 = sorted(s3)
s4 = sorted(s4)
for i in range(s1-1):
    if s2[i] != s3[i]:
        print(s2[i])
        break
    elif i == s1-2:
        print(s2[i+1])
for i in range(s1-2):
    if s3[i] != s4[i]:
        print(s3[i])
        break
    elif i == s1-3:
        print(s3[i+1])

s1 = int(input())
s2 = [int(i) for i in input().split()]
for i in range(len(s2)):
    if s2[i]:
        print('HARD')
        break
    if i+1==len(s2):
        print('EASY')


s = [int(i) for i in input().split()]
if s[2]>=s[1]>=s[0] or s[0]>=s[1]>=s[2]:
    print(abs(s[2]-s[0]))
elif s[2]>=s[0]>=s[1] or s[1]>=s[0]>=s[2]:
    print(abs(s[2]-s[1]))
else:
    print(abs(s[1]-s[0]))


words = input().upper().split()
lists = []
s = ''
for i in range(len(words)):
    lists.append(list(words[i]))
    s += '-'.join(lists[i])
    if not i+1 == len(words):
        s += ' '
print(s)


f=open("INPUT.TXT", "r")
s = f.read()
l = len(s)
f.close()
f=open("OUTPUT.TXT", "w")
for i in range(l//2):
    if s[i] != s[-(i+1)]:
        f.write('NO')
        break
    elif i+1 == l//2:
        f.write('YES')
f.close()


f=open("INPUT.TXT", "r")
start = f.readline().split()
end = f.readline().split()
f=open("OUTPUT.TXT", "w")
if start[0] == end[0] or start[1] == end[1]:
    f.write('YES')
else:
    f.write('NO')
f.close()



words = input().upper().split()
lists = []
s = ''
for i in range(len(words)):
    lists.append(list(words[i]))
    s += '-'.join(lists[i])
    if not i+1 == len(words):
        s += ' '
print(s)
"""

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