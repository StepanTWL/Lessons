"""
english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for index, word in enumerate(english_words,1):
    print(f'Word № {index} = {word}')


arr=list(enumerate([int(a) for a in input()],1))
arr1=[]
for i in range(len(arr)):
    if not i%2:
        if arr[i][1]*2 > 9:
            arr1.append(arr[i][1]*2-9)
        else:
            arr1.append(arr[i][1]*2)
    else:
        arr1.append(arr[i][1])


a=sum(arr1)
a%=10
if sum(arr1)%10:
    print('False')
else:
    print('True')



def keanu_reeves() ->str:
    return print(f"YOU'RE BREATHTAKING")
keanu_reeves()



def summa_n(t:int) -> str:
    S=sum(range(t+1))
    return print(f"Я знаю, что сумма чисел от 1 до {t} равна {S}")

summa_n(5)




def check_password(s:str) -> str:
    count=0
    if len(s)<10:
        return print('Easy peasy')
    if s.islower():
        return print('Easy peasy')
    for i in s:
        if i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='*' or i.isalnum():
            continue
        else:
            return print('Easy peasy')
    for i in s:
        if i.isdecimal():
            count += 1
    if count<3:
        return print('Easy peasy')
    else:
        return print('Perfect password')

check_password(input())


def count_letters(s:str) -> str:
    N=0
    K=0
    for i in s:
        if i.islower():
            K+=1
        elif i.isalpha():
            N+=1
    return print(f"Количество заглавных символов: {N}\nКоличество строчных символов: {K}")


from functools import reduce
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(reduce(gcd, arr))


def find_duplicate(arr:list) -> list:
    dictt=dict()
    arr1=[]
    for i in arr:
        if dictt.get(i)==None:
            dictt[i] = 1
        else:
            dictt[i] = dictt.get(i) + 1
    for i in dictt:
        if dictt.get(i)>1:
            arr1.append(i)
    return arr1

arrr=[1,2,3,2,1,3,4,5,6,5,4,3,2,6,7,8,9]
print(find_duplicate(arrr))



def first_unique_char(s:str) -> int:
    dicct=dict()
    s=s.lower()
    for i in range(len(s)):
        if dicct.get(s[i])==None:
            dicct[s[i]] = 1
        else:
            dicct[s[i]] = dicct.get(s[i]) + 1
    for i in dicct:
        if dicct[i]==1:
            return s.find(i)
    return -1

ss='abracadabra'
print(first_unique_char(ss))


#format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa и Maggie'
def format_namelist(arr:list) -> str:
    s=''
    count=0
    indexx=0
    for i in arr:
        if not i.get('name')==None:
            s+=i.get('name') + ', '
            count += 1
    if count > 0:
        s=s[:-2]
    if count > 1:
        indexx=s.rfind(', ')
        s=s[:indexx] + ' и ' + s[indexx+2:]
    return s

print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))


def domain_name(url:str) -> str:
    url=url.lower()
    if url.count('www.')>0:
        indexx=url.index('www.')+4
    elif url.count('//')>0:
        indexx=url.index('//')+2
    indexx1=url.find('.', indexx)
    return url[indexx:indexx1]

print(domain_name("http://google.com")) # возвращает "google"
print(domain_name("http://google.co.jp")) # возвращает  "google"
print(domain_name("www.xakep.ru")) # возвращает "xakep"
print(domain_name("https://youtube.com")) # возвращает "youtube"
print(domain_name("https://www.asos.com")) # возвращает "asos"
print(domain_name("http://www.lenovo.com"))# возвращает "lenovo"


from math import factorial
def trailing_zeros(n:int) -> int:
    s=str(factorial(n))
    count=0
    for i in range(-1, -len(s)-1, -1):
        if s[i]=="0":
            count+=1
        else:
            break
    return count

print(trailing_zeros(6))
print(trailing_zeros(10))
print(trailing_zeros(20))


def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    indexx=ord(letter)+shift
    if 97<=indexx<=122:
        return chr(indexx)
    elif indexx<97:
        indexx=(indexx-97)%26
    else:
        indexx=(indexx-123)%26
    return chr(indexx+97)

print(shift_letter('b',1))#c
print(shift_letter('b',-1))#a
print(shift_letter('b',27))#c
print(shift_letter('b',-27))#a


def print_goods(*args):
    count=0
    for i in args:
        if isinstance(i, str):
            if i.isalpha():
                count+=1
                print(str(count)+'. '+i)
    if not count:
        print('Нет товаров')

print_goods('apple', 'banana', 'orange')
print_goods(1, True, 'Грушечка', '', 'Pineapple') 
print_goods([], {}, 1, 2) 


def info_kwargs(**kargs):
    dictt=dict()
    arr=[]
    for key, value in kargs.items():
        dictt[key]=value
    for key in kargs.keys():
        arr.append(key)
    arr=sorted(arr)
    for i in arr:
        print(i+' = '+str(dictt[i]))

info_kwargs(first_name="John", last_name="Doe", age=33) 


def rec(arr: list) -> list:
    if len(arr)>0:
        print(arr.pop(), end=" ")
        rec(arr)

input()
arr1=list(map(int, input().split()))
rec(arr1)


def fibo(num: int, ex0: int = 0, ex1: int = 1) -> int:
    if num==0:
        return ex0
    elif num==1:
        return ex1
    else:
        num -= 1
        return fibo(num, ex1, ex0+ex1)

n=int(input())
print(fibo(n))


def list_sum_recursive(arr: list) -> int:
    if not len(arr):
        return 0
    elif len(arr)>1:
        arr[-1]=arr[-2]+arr.pop()
        list_sum_recursive(arr)
    return arr[0]

print(list_sum_recursive([1,2,3,4]))



def flatten(arr: list) -> list:
    if not arr:
        return []
    if isinstance(arr[0], list):
        return flatten(arr[0])+flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])

print(flatten([2,[[[1]]],3]))


from typing import List
def merge_two_list(a: List[int], b: List[int]) -> List[int]:
    i = 0
    j = 0
    arr = []
    while i != len(a) and j != len(b):
        if a[i] > b[j]:
            arr.append(b[j])
            j += 1
        elif a[i] < b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(a[i])
            arr.append(b[j])
            i += 1
            j += 1
        if i == len(a):
            while j != len(b):
                arr.append(b[j])
                j += 1
            break
        elif j == len(b):
            while i != len(a):
                arr.append(a[i])
                i += 1
            break
    return arr


def merge_sort(s: List[int]) -> List[int]:
    if len(s)>1:
        return merge_two_list(merge_sort(s[:len(s)//2]), merge_sort(s[len(s)//2:]))
    else:
        return s


arr=list(map(int, input().split()))
print(merge_sort(arr))


from typing import List
def merge_two_list(a: List[int], b: List[int]) -> List[int]:
    arr = []
    while len(a) and len(b):
        if a[0] > b[0]:
            arr.append(b.pop(0))
        elif a[0] < b[0]:
            arr.append(a.pop(0))
        else:
            arr.append(a.pop(0))
            arr.append(b.pop(0))
        if not len(a):
            while len(b):
                arr.append(b.pop(0))
            break
        elif not len(b):
            while len(a):
                arr.append(a.pop(0))
            break
    return arr


def merge_sort(s: List[int]) -> List[int]:
    if len(s)>1:
        return merge_two_list(merge_sort(s[:len(s)//2]), merge_sort(s[len(s)//2:]))
    else:
        return s


arr=list(map(int, input().split()))
print(merge_sort(arr))


from typing import List
def quick_sort(s: List[int]) -> List[int]:
    if not len(s):
        return None
    elif len(s)==1:
        return s
    elif len(s)==2:
        if s[0]>s[1]:
            s.append(s.pop(0))
        return s
    oporn=s[len(s)//2:len(s)//2+1]
    arr1=[]
    arr2=[]
    for i in range(len(s)):
        if i==len(s)//2:
            continue
        elif s[i] > oporn[0]:
            arr2.append(s[i])
        else:
            arr1.append(s[i])
    if not len(arr2):
        return quick_sort(arr1)+oporn
    elif not len(arr1):
        return oporn+quick_sort(arr2)
    return quick_sort(arr1)+oporn+quick_sort(arr2)

    

s=[19, 4, 5, 17, 1]
print(quick_sort(s))


def text_decor(func):

    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')
    
    return inner

@text_decor
def simple(n):
    print('lol'*n)

simple(5)


def repeater(func):

    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return inner


def double_it(func):

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*2

    return inner

@double_it
def mult(a,b):
    return a*b

res = mult(4,6)
print(res)


def file_read(s: str):
    with open(s, 'r') as file:
        file.read()
        file.close()

file_read('myfile.txt')



import json
with open('manager_sales.json') as file:
    data = json.load(file)
maxx=0
maxx_index=0
for i in range(len(data)):
    sum=0
    for j in data[i]['cars']:
        sum+=j['price']
    if sum>maxx:
        maxx_index=i
        maxx=sum

print(data[maxx_index]['manager']['first_name']+' '+ data[maxx_index]['manager']['last_name']+' '+str(maxx))
file.close()


import json
with open('group_people.json') as file:
    data = json.load(file)
count=[]

for i in range(len(data)):
    count.append(0)
    for j in data[i]['people']:
        if j['year']>1977 and j['gender']=='Female':
            count[-1]+=1
print(count.index(max(count))+1, max(count))
"""

import json
with open('Abracadabra__1_.txt', 'r') as file:
    s=file.read()
    file.close()
with open('Alphabet.json', 'r') as file:
    data=json.load(file)
    file.close()
for i in range(len(s)):
    if not data[s[i]]==None:
        if not i:
            s=data[s[i]]+s[i+1:]
        elif i==len(s)-1:
            s=s[:i]+data[s[i]]
        else:
            s=s[:i]+data[s[i]]+s[i+1:]

print(s)
