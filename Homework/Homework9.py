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
"""

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