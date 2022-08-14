def fact(x):
    if x==1:
        return 1
    return fact(x-1)*x

print(fact(10))

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2) 

def palindrom(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom('qwerewq'))

def pow(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/pow(x,-n)
    if n%2==0:
        return pow(x,n//2)*pow(x,n//2)
    else:
        return pow(x,n-1)*x

print(pow(2,-10))


a=[1,2,[3,4,[5,6,[7,8],9,10],11,12],13,14,[15,[16,[24,[25,[26]]]],17],[18,[19,[20],21],22],23]

def rec(lists, level=1):
    print(*lists,'level=',level)
    for i in lists:
        if type(i)==list:
            rec(i,level+1)

rec(a)

import os
path = 'movies'

def obhFile(path,level=1):
    print('Level=',level,'Content:',os.listdir(path))
    for i in os.listdir(path):
       if os.path.isdir(path+'\\'+i):
        print('Спускаемся', path+'\\'+i)
        obhFile(path+'\\'+i,level+1)
        print('Возращаемся в',path)

obhFile(path)

print(os.listdir(path))

def rec(s):
    if len(s)==1 or len(s)==2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]

s = input()
print(rec(s))