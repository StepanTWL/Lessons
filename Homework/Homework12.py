"""
words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error', 
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government', 
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']
count = 0
words = set(words)
for i in words:
    if len(i) > 6:
        count += 1
        
print(count)



n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    print(len(set(arr[i])))


n = int(input())
arr = set()
sum = 0
for i in range(n):
    arr.update(set(map(int, input().split())))
print(len(arr))


arr = list(map(str, input().lower().split(',')))
arr1 = set()
for i in arr:
    if i in arr1:
        print('ДА')
    else:
        print('НЕТ')
    arr1.add(i)
pass


def get_body_mass_index(mass, rost):
    if not rost:
        print("Избыточная масса тела")
        return
    if mass/((rost/100)**2) < 18.5:
        print("Избыточная масса тела")
        return
    if 18.5 <= mass/((rost/100)**2) <= 25:
        print("Норма")
        return
    if mass/((rost/100)**2) > 25:
        print("Избыточная масса тела")
        return

get_body_mass_index(0, 50)


lang = int(input())

match lang:#rabotaet s 3.10
    case 1:
        print('Совсем еще зеленый студентик')
    case 2:
        print('Джун-студент')
    case 3:
        print('Мидл-студент')
    case 4:
        print('Сеньер-студент')
    case 5:
        print('Босс качалки')
    case _:
        print('Неизвестный курс')

lang = int(input())

match lang:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('31')
    case 4 | 6 | 9 | 11:
        print('30')
    case 2:
        print('28')
    case _:
        print('0')


if (money := int(input())) > 10000:
    print (f"Ого! {money}! Куда вам столько? Мы заберем {money - 10000}")
else:
    print (f"Сумма {money} не превышает лимит, проходите")

print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')



n=int(input())
k=int(input())
arr=[i for i in range(1,n+1)]
count = k-1
while len(arr)>1:
    while count>=len(arr):
        count = count-len(arr)
    arr.pop(count)
    count+=k-1
print(*arr)


a=b=c=d=0
n=int(input())
for i in range(n):
    x,y = list(map(str, input().split()))
    if x[0]=='-':
        x=-1*int(x[1:])
    else:
        x=int(x)
    if y[0]=='-':
        y=-1*int(y[1:])
    else:
        y=int(y)
    if x>0 and y>0:
        a+=1
    elif x<0 and y>0:
        b+=1
    elif x<0 and y<0:
        c+=1
    elif x>0 and y<0:
        d+=1
print(f"Первая четверть: {a}")
print(f"Вторая четверть: {b}")
print(f"Третья четверть: {c}")
print(f"Четвертая четверть: {d}")


count=0
arr=list(map(int, input().split()))
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        count+=1
print(count)


arr=list(map(int, input().split()))
for i in range(len(arr)//2):
    arr[i*2], arr[i*2+1] = arr[i*2+1], arr[i*2]
print(*arr)


arr=list(map(int, input().split()))
arr1=[0]*len(arr)
for i in range(len(arr)):
    if i==len(arr)-1:
        arr1[0] = arr[i]
    else:
        arr1[i+1] = arr[i]
print(*arr1)



n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
mul=int(input())
suc=0
for i in range(n):
    for j in range(n):
        if arr[i]*arr[j]==mul and not i==j:
            suc=1
            break
    if suc:
        break
if suc:
    print('ДА')
else:
    print('НЕТ')


s1=input()
s2=input()
if s1==s2:
    print('ничья')
elif (s1=='камень' and s2=='ножницы') or (s1=='бумага' and s2=='камень') or (s1=='ножницы' and s2=='бумага'):
    print('Руслан')
else:
    print('Тимур')


# камень, ножницы, бумага, ящерица, Спок
rules_game = {
    'камень'    :[['ножницы', 'ящерица'],   ['бумага', 'Спок']],
    'ножницы'   :[['ящерица', 'бумага'],    ['камень', 'Спок']],
    'бумага'    :[['Спок', 'камень'],       ['ящерица', 'ножницы']],
    'ящерица'   :[['Спок', 'бумага'],       ['камень', 'ножницы']],
    'Спок'      :[['ножницы', 'камень'],    ['ящерица', 'бумага']],
}

s1=input()
s2=input()

if s2 in rules_game[s1][0]:
    print('Тимур')
elif s2 in rules_game[s1][1]:
    print('Руслан')
else:
    print('ничья')


maxO=maxP=0
countO=countP=0
s=input()
if len(s):
    for i in s:
        if i=='Р':
            countP += 1
        else:
            if countP > maxP:
                maxP = countP
            countP = 0
    if countP > maxP:
        maxP = countP
    print(maxP)

else:
    print(0)


n=int(input())
arr=[]
num=[]
for i in range(n):
    flag=0
    arr.append(input())
    for j in 'anton':
        if j in arr[i]:
            arr[i] = arr[i][arr[i].find(j)::]
            flag+=1
    if flag == 5:
        num.append(i+1)
print(*num)        



s=input()
s+=' запретил букву '
letter='абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in letter:
    if i in s:
        print(s+i)
        s=s.replace(i,'')
        s=s.lstrip()
        while '  ' in s:
            s=s.replace('  ', ' ')
"""