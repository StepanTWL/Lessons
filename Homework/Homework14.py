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



sec=input()
my_dict = {}
my_dict1 = {}
n=int(input())
for i in range(n):
    s=input()
    my_dict[s[3]] = s[0]
for i in sec:
    my_dict1[i] = str(sec.count(i))
word = ''
for i in sec:
    word += my_dict[my_dict1[i]]
print(word)


numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i]**2 for i in range(len(numbers))}


colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
result = {color: colors[color] for color in colors if colors[color] != None}


favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
result = {number: favorite_numbers[number] for number in favorite_numbers if 9<favorite_numbers[number]<100}


months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {months[month]: month for month in months}


s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i[:i.find(':')]): i[i.find(':')+1:] for i in list(map(str, s.split()))}


numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {i: [j for j in range(1,i+1) if i%j==0] for i in numbers}


words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {word: [ord(letter) for letter in word] for word in words}


letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {letter: letters[letter] for letter in letters if not letter in remove_keys}


students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
result = {student: students[student] for student in students if students[student][0]>167 and students[student][1]<75}
"""

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {tuple[0]: tuples[tuple] for tuple in tuples}


pass
