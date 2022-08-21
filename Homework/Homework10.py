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
"""

def rec(arr: list) -> list:
    if len(arr)>0:
        print(arr.pop(), end=" ")
        rec(arr)

input()
arr1=list(map(int, input().split()))
rec(arr1)
