"""
s = input().lower()# Девушка или Юноша
arr = [0]*26
count = 0
for i in s:
    arr[ord(i)-97] += 1
for i in range(len(arr)):
    if not arr[i] == 0:
        count += 1
if count%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')


number = int(input())#Почти счастливое число
count = 0
error = 0
while number > 0:
    if number%10 == 4 or number%10 == 7:
        count += 1
    number //= 10
if count == 0:
    error = 1
while count > 0:
    if not count%10 == 4 and not count%10 == 7:
        error = 1
    count //= 10
if error:
    print('NO')
else:
    print('YES')


#I Wanna Be the Guy
max_lvl = int(input())
lvl = []
lvl1 = [0]*max_lvl
error = 0
for i in range(2):
    lvl.append(list(map(int, input().split())))
for i in range(2):
    for j in range(1, lvl[i][0]+1):
        lvl1[lvl[i][j]-1] += 1
for i in lvl1:
    if i == 0:
        error = 1
if error:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')


#Счастливое деление
number = int(input())
delets = []
delet = 4
error = 0
while delet < 1000:
    delet1 = delet
    error = 0
    while delet1 > 0:
        if not delet1%10 == 4 and not delet1%10 == 7:
            error = 1
        delet1 //= 10
    if not error:
        delets.append(delet)
    delet += 1
for i in delets:
    if number%i == 0:
        error = 0
        break
    error = 1
if error:
    print('NO')
else:
    print('YES')


#Find Numbers with Even Number of Digits
def even(n):
    i = 1
    while n > 0:
        n //= 10
        i += 1
    return i%2

num = list(map(int, input().split()))
count = 0
for i in num:
    if even(i):
        count += 1
print(count)


#Система регистрации
number = int(input())
names = ''
base = {}
for i in range(number):
    names = input()
    if not base.setdefault(names):
        base.update({names : 'OK'})
    else:
        for i in range(1, 10000):
            if not base.setdefault(names+str(i)):
                base.update({names+str(i) : names+str(i)})
                break
x = list(base.values())
for i in range(number):
    print(x[i])


#Система регистрации
number = int(input())
base = {}
for i in range(number):
    name = input()
    if not name in base:
        base[name] = 'OK'
    else:
        for i in range(1, 10000):
            if not name+str(i) in base:
                base[name+str(i)] = name+str(i)
                break
x = list(base.values())
for i in range(number):
    print(x[i])


#771. Jewels and Stones
def find(j, s):
    count = 0
    for i in j:
        count += s.count(i)
    return(count)

jewels, stones = input().split(', ')
jewels_new = jewels[jewels.find('"')+1:jewels.rfind('"')]
stones_new = stones[stones.find('"')+1:stones.rfind('"')] 
print(find(jewels_new, stones_new))


def find(j, s):
    count = 0
    for i in j:
        count += s.count(i)
    return(count)

jewels = input()
stones = input()
print(find(jewels, stones))


#Find Numbers with Even Number of Digits
def even(n):
    i = 1
    while n > 0:
        n //= 10
        i += 1
    return i%2

num = list(map(int, input().split()))
count = 0
for i in num:
    if even(i):
        count += 1
print(count)


#1313. Decompress Run-Length Encoded List
nums = list(map(int, input().split()))
arr = []
for i in range(len(nums)//2):
    for j in range(nums[i*2]):
        arr.append(nums[i*2+1])
print(arr)



#A. Эпическая игра
from math import gcd
semen, antisemen, stone = list(map(int, input().split()))
x = 0
while stone >= 0:
    stone -= gcd(semen, stone)
    if stone < 0:
        x = 1
    stone -= gcd(antisemen, stone)
print(x)



def f(s):
    if len(s)==1 or len(s)==0:
        return s
    if len(s)==2:
        return s[0]+'*'+s[1]
    return s[0]+'*'+f(s[1:-1])+'*'+s[-1]

str = input()
print(f(str))


count = 0
def f(num, cnt):
    sum = 0
    if num//10==0:
        return num, cnt
    while num>0:
        sum += num%10
        num //= 10
    cnt += 1
    return f(sum, cnt)

number = int(input())
for i in f(number, count):
    print(str(i), end=' ')


def f(s):
    if len(s)==1 or len(s)==0:
        return s
    if len(s)==2:
        return s[0]+'*'+s[1]
    return s[0]+'*'+f(s[1:-1])+'*'+s[-1]

str = input()
print(f(str))

#Зеркальная строка
def f(s):
    if len(s)==0:
        return s
    return s[0]+f(s[1:])+s[0]

str = input()
print(f(str))


n = int(input())
arr = [i**2 for i in range(n)]
for i in arr:
    print(i)

nums = list(map(int, input().split()))
for i in range(len(nums)):
    nums[i] **= 3
print(' '.join([str(i) for i in nums]))


def recurs(num, arr=[]):

    if num == 0:
        return print(arr)
    else:
        for i in range(1, num+1):
            if not arr:
                recurs(num-i, arr+[i])
            elif arr[-1] >= i:
                recurs(num-i, arr+[i])

n = int(input())
recurs(n)
"""


num1=int(input())
arr1=list(map(int, input().split()))
num2=int(input())
arr2=list(map(int, input().split()))

