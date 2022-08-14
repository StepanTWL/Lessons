"""
s = input()
number = int(input())
for i in range(number):
    print(s)


count = int(input())
s = []
pas = 0
max_pas = 0
for i in range(count):
    s.append([0]*2)
    s[i] = [int(x) for x in input().split()]
    pas = pas - s[i][0] + s[i][1]
    if max_pas < pas:
        max_pas = pas
print(max_pas)


a = int(input())
b = int(input())
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


number, unit = [int(x) for x in input().split()]
while unit > 0:
    if number % 10 > 0:
        number -= 1
    else:
        number //= 10
    unit -=1
print(number)


count = int(input())
island = 1
past_size = -1
while count > 0:
    unit = int(input())
    if past_size == unit // 10:
        island += 1
    past_size = unit % 10
    count -= 1
print(island)


s = input()
s = list(s)
for i in range(len(s)):
    if i % 3 == 0:
        s[i] = ''
s = ''.join(s)
print(s)


count = int(input())
arr = [int(x) for x in input().split()]
police = 0
fail = 0
for i in range(len(arr)):
    if arr[i] > 0:
        police += arr[i]
    elif arr[i] == -1 and police > 0:
        police -= 1
    elif arr[i] == -1 and police == 0:
        fail += 1
print(fail)


count, number = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
n = 0
for i in range(count):
    if arr[i] >= arr[number-1] and arr[i] > 0:
        n += 1
print(n)


s = input().lower()
for i in "aoyeui":
    s = s.replace(i, '')
s = '.'+ '.'.join(list(s))
print(s)


podk = [int(i) for i in input().split()]
max = 0
for i in podk:
    if max < podk.count(i):
        max = podk.count(i)
print(max-1)


count, games = [int(i) for i in input().split()]
command = [int(i) for i in input().split()]
max_games = 5
number_member_in_command = 3
command.sort()
for i in range(count):
    if command[i]+games > max_games:
        print(i//3)
        break
    elif i+1 == count:
        print(count//3)



numbers = [int(i) for i in input().split()]
s = []
for i in range(len(numbers)//2):
    s.append([numbers[2*i+1]]*numbers[2*i])
print([item for i in s for item in i])


number1 = input()
number2 = input()
number = ''
for i in range(len(number1)):
    if number1[i] == number2[i]:
        number += '0'
    else:
        number += '1'
print(number)


count = int(input())
brus = [int(i) for i in input().split()]
brus.sort()
max = 0
new = []
for i in range(count):
    if max < brus.count(brus[i]):
        max = brus.count(brus[i])
    if new.count(brus[i]) == 0:
        new.append(brus[i])
print(max, len(new))


count = int(input())
win = input().lower()
if win.count('a') > win.count('d'):
    print('Anton')
elif win.count('a') < win.count('d'):
    print('Danik')
else:
    print('Friendship')


s = input()
l = 0
h = 0
for i in s:
    if ord('a')<=ord(i)<=ord('z'):
        l +=1
    else:
        h +=1
if l >= h:
    print(s.lower())
else:
    print(s.upper())
"""


count = int(input())
s = ''
arr = []
status = 'NO'
for i in range(count):
    s = input()
    if s.count('OO'):
        status = 'YES'
        if s.index('OO'):
            arr.append(s[:3]+'++')
        else:
            arr.append('++'+s[2:])
    else:
        arr.append(s)
print(status)
for i in range(count):
    print(arr[i])


