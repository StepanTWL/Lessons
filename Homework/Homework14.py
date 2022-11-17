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


tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {tuple[0]: tuple[1:] for tuple in tuples}


student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#results = [i for i in zip(student_ids, student_names, student_grades)]
#result = [{result[0]: {result[1]: result[2]}} for result in results]
result = [{i[0]: {i[1]: i[2]}} for i in zip(student_ids, student_names, student_grades)]
#[{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...]



import random

length = int(input())    # длина пароля
s=''
for i in range(length):
    n = 91
    while n > 90 and n < 97:
        n = random.randint(65,122)
    s += chr(n)
print(s)



import random
import string

def generate_index():
    return f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.digits)}_{random.choice(string.digits)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"


import random

arr=[]
for i in range(100):
    n=random.randint(1000000, 9999999)
    while n in arr:
        n = random.randint(1000000, 9999999)
    arr.append(n)
    print(arr[-1])


import random

arr = list(input())
random.shuffle(arr)
print(*arr, sep='')

import random

arr=[[0]*5 for i in range(5)]
arr1=[]
for i in range(5):
    for j in range(5):
        if i==j==2:
            arr[i][j]=0
        else:
            n = random.randint(1, 75)
            while n in arr1:
                n=random.randint(1, 75)
            arr[i][j]=n
            arr1.append(n)
for i in range(5):
    for j in range(5):
        print(str(arr[i][j]).ljust(3), end='')
    print()

import random

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
random.shuffle(arr)
for i in range(n):
    if i==n-1:
        print(f'{arr[i]} - {arr[0]}')
    else:
        print(f'{arr[i]} - {arr[i+1]}')


import random
from string import ascii_uppercase, ascii_lowercase, digits
from typing import List

LETTER = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
          'en': [x for x in ascii_lowercase if x not in 'ol'],
          'dig': [x for x in digits if x not in '01']}

def generate_password(length: int) -> str:
    s = random.choice(LETTER['EN']) + random.choice(LETTER['en']) + random.choice(LETTER['dig'])
    for i in range(length-3):
        n = random.randint(50, 122)
        while 57 < n < 65 or 90 < n < 97 or n == 73 or n == 79 or n == 108 or n == 111:
            n = random.randint(50, 122)
        s += chr(n)
    return s


def generate_passwords(count: int, length: int) -> List[str]:
    arr = []
    for i in range(count):
        arr.append(generate_password(length))
    return arr


n = int(input())
m = int(input())
print(*generate_passwords(n, m), sep='\n')


import random

n = 10**6       # количество испытаний
m = 0
for i in range(n):
    x = random.uniform(-2.0, 2.0)
    y = random.uniform(-2.0, 2.0)
    if (-2 <= x <= 2) and (-2 <= y <= 2) and (x**3+y**4+2 >= 0) and (3*x+y**2 <= 2):
        m += 1
print(16*m/n)

import random

n = 10 ** 6  # количество испытаний
m = 0
for i in range(n):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 <= 1:
        m += 1
print(4 * m / n)


from decimal import *

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
arr = list(map(Decimal, s.split()))
print(max(arr)+min(arr))


from decimal import *
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
arr = list(map(Decimal, s.split()))
arr = sorted(arr, reverse=True)
print(sum(arr))
print(*arr[:5])


from decimal import *
num = Decimal(input())
if abs(num) > 1:
    print(max(num.as_tuple().digits)+min(num.as_tuple().digits))
else:
    print(max(num.as_tuple().digits))


from decimal import *
num = Decimal(input())
print(num.exp()+num.ln()+num.log10()+num.sqrt())


from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for i in numbers:
    print(f'{i} = {Fraction(i)}')


from fractions import Fraction
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
arr = list(map(Fraction, s.split()))
print(max(arr)+min(arr))

from fractions import Fraction

m = int(input())
n = int(input())
print(Fraction(m, n))

from fractions import Fraction

a = input()
b = input()
print(f'{a} + {b} = {Fraction(a)+Fraction(b)}')
print(f'{a} - {b} = {Fraction(a)-Fraction(b)}')
print(f'{a} * {b} = {Fraction(a)*Fraction(b)}')
print(f'{a} / {b} = {Fraction(a)/Fraction(b)}')

from fractions import Fraction
from math import factorial

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += Fraction(1, factorial(i))
print(sum)

from fractions import Fraction
from math import gcd

arr = []
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j == n and i < j and gcd(i, j)==1:
            arr.append(Fraction(i, j))
print(max(arr))
"""
from fractions import Fraction
from math import gcd

arr = []
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j and gcd(i, j) == 1:
            a = Fraction(i, j)
            arr.append(a)
sorted(arr)
for i in arr:
    print(i)
pass
