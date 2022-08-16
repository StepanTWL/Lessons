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
"""

n=input()
n_=input()
dict={}
dict_={}
if len(n)==len(n_):
    for i in n:
        dict[i]=dict.get(i, 0) + 1
    for i in n_:
        dict_[i]=dict_.get(i, 0) + 1
    keys=dict.keys()
    keys_=dict_.keys()
    for 