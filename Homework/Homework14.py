"""
def double_fact(n :int) ->int:#факториал
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n*double_fact(n-2)
    


dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict1.copy()
for i in result:
    if i in dict2:
        result[i] += dict2[i]
        dict2.pop(i)
result.update(dict2)
pass



s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

arr=s.split()
my_dict = {}
for i in arr:
    my_dict[i] = s.count(i)
maxx = max(my_dict.values())
arr1=[]
for i in my_dict:
    if my_dict[i] == maxx:
        arr1.append(i)
print(sorted(arr1)[0])



pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in range(len(pets)):
    result.setdefault(pets[i][1:], []).append(pets[i][0])


arr=[word.strip('.,!?:;-') for word in input().lower().split()]
my_dict = {}
for i in arr:
    my_dict[i] = arr.count(i)
minn = min(my_dict.values())
arr1=[]
for i in my_dict:
    if my_dict[i] == minn:
        arr1.append(i)
print(sorted(arr1)[0])


arr=input().split()
my_dict = {}
for i in arr:
    my_dict[i] = my_dict.get(i,-1)+1
    if my_dict[i]:
        print(f'{i}_{my_dict[i]}', end=' ')
    else:
        print(i, end=' ')


n=int(input())
my_dict = {}
for i in range(n):
    s=input()
    my_dict[s[:s.index(':')].lower()] = s[s.index(':')+2:]
m=int(input())
arr=[]
for i in range(m):
    arr.append(input().lower())
for i in arr:
    if i in my_dict:
        print(my_dict[i])
    else:
        print('Не найдено')


s1=input()
s2=input()
my_dict1 = {}
my_dict2 = {}
for i in set(s1):
    my_dict1[i] = s1.count(i)
for i in set(s2):
    my_dict2[i] = s2.count(i)
if my_dict1==my_dict2:
    print('YES')
else:
    print('NO')


s1=input().lower()
s2=input().lower()
my_dict1 = {}
my_dict2 = {}
for i in set(s1):
    if i.isalpha():
        my_dict1[i] = s1.count(i)
for i in set(s2):
    if i.isalpha():
        my_dict2[i] = s2.count(i)
if my_dict1==my_dict2:
    print('YES')
else:
    print('NO')


n=int(input())
my_dict = {}
for i in range(n):
    s=input()
    my_dict[s[:s.index(' ')]] = s[s.index(' ')+1:]
    my_dict[s[s.index(' ')+1:]] = s[:s.index(' ')]
print(my_dict[input()])


n=int(input())
my_dict = {}
for i in range(n):
    arr=input().split()
    for j in range(len(arr)-1):
        my_dict[arr[j+1]] = arr[0]
m=int(input())
arr1=[]
for i in range(m):
    arr1.append(input())
for i in arr1:
    print(my_dict[i])


n=int(input())
my_dict = {}
for i in range(n):
    arr=input().lower().split()
    my_dict.setdefault(arr[1],[])
    my_dict[arr[1]].append(arr[0])
m=int(input())
arr1=[]
for i in range(m):
    arr1.append(input().lower())
for i in arr1:
    if i in my_dict:
        print(*my_dict[i])
    else:
        print('абонент не найден')
"""


sec=set(input())
my_dict = {}
for i in sec:
    
n=int(input())
my_dict1 = {}
for i in range(n):
    arr=input().split(': ')
    my_dict1[arr[0]] = arr[1]
pass
