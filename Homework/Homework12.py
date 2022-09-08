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
"""

if (money := int(input())) > 10000:
    print (f"Ого! {money}! Куда вам столько? Мы заберем {money - 10000}")
else:
    print (f"Сумма {money} не превышает лимит, проходите")

print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')