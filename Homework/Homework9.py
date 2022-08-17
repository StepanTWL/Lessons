"""
account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}

keys=[]
for i in account.keys():
    keys.append(i)
print(keys)


d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d1.update(d2)
d2=d1.copy()
print(d2)


countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
countrie=''
stop=0
for i in countries.keys():
    countrie = i
    for j in countries.get(i):
        if j==city:
            stop=1
            break
    if stop:
        break
    countrie='' 
if countrie:
    print(f'INFO: {city} is a city in {countrie}')
else:
    print(f'ERROR: Country for {city} not found')


user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}
user_new=dict()
password=user.pop('password')
last_name=user.pop('last_name')
for i in user:
    if i=='first_name':
        user_new['secret'] = password
    elif i=='username':
        user_new['surname'] = last_name
    user_new[i]=user[i]
user.clear()
for i in user_new:
    user[i]=user_new[i]
print()



workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}

keys=workers.keys()
for i in keys:
    if workers[i]['name']=='Brad':
        workers[i]['salary'] = 8500
print(workers)


n=input()
dict={}
for i in n:
    if i.isalpha():
        dict[i] = dict.get(i, 0) + 1
print(dict)


supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
sum=0
keys=supermarket.keys()
for i in keys:
    sum += supermarket[i]['quantity']*supermarket[i]['price']
print(sum)

s1=input()
s2=input()
d1={s: s1.count(s) for s in s1}
d2={s: s2.count(s) for s in s2}
print('YES' if d1==d2 and len(d1)==len(d2) else 'NO')


morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
n=input().lower().split()
for i in s:
    for j in i:
        print(morze[j], end=' ')
    print()



persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'), 
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'), 
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'), 
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'), 
    ('Amber Perez', 403445, 'M', '0602870126')
]

data={}
for i in persons:
    data[i[0]]={'salary': i[1], 'gender': i[2], 'passport': i[3]}
print()


from pprint import pprint
data = {'my_friends': {'count': 10,
                       'people': [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
                                 {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
                                 {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
                                 {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
                                 {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
                                 {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин',
                                  'bdate': '6.12.1982'},
                                 {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова',
                                  'bdate': '4.11.1995'},
                                 {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
                                 {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
                                 {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова',
                                  'bdate': '20.12'}]}}
arr=sorted([i['first_name']+'\n' for i in data['my_friends']['people']])
for i in arr:
    print(i)



user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}
arr=input().lower().split()
dictt={i: user[i] for i in arr}
print(dictt)


people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book={i[1]: i[0] for i in people}
print(phone_book)


vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
vector1 = [vector[i][j] for i in range(len(vector)) for j in range(len(vector[i]))]
print(vector1)


s=input()
sett=set([i for i in s if '0'<=i<='9'])
countt=0
suc=0
arr=[]
for i in sett:
    if s.count(i) > 1:
        suc=1
        arr.append(i)
if suc:
    print(*(sorted(arr)))
else:
    print('NO')


s=input()
sett=set(s)
for i in sett:
    while s.count(i) > 1:
        s = s[:s.rindex(i)]+s[s.rindex(i)+1:]
print(s)
"""

sett=set()
dictt=dict('Билл': 0, 'Вилл': 0, 'Дилл': 0)
arr=[]
arr.append
while True:
    s = input()
    if s == 'конец':
        break
    sett.add(s)
for i in sett:
    dictt[i[:i.index(':')]] = dictt.get(i[:i.index(':')], 0) + 1
for i in dictt.keys():
    arr.append(i)
sorted(arr, reverse=True)
for i in arr:
    print('Количество уникальных комментаторов у '+i+' - '+str(dictt[i]))