


from multiprocessing.sharedctypes import Value


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
