from datetime import datetime
import json

str_json = """
{
    "response": {
        "count": 5961878,
        "items": [{
            "first_name": "Елизавета",
            "id": 620471795,
            "last_name": "Сопова"
        }, {
            "first_name": "Роман",
            "id": 614752515,
            "last_name": "Малышев"
        }]
    }
}"""

data = json.loads(str_json)
print(data['response']['count'])
for i in data['response']['items']:
    print(i['first_name'], i ['last_name'])
    del i['id']
    i['likes'] = 50
    i['a']=None#в json будет null
    i['data']=datetime.now().strftime('%d.%m.%y')

new_json = json.dumps(data, indent=2)
print(new_json)

with open('my_json', 'w') as file:
    json.dump(data,file, indent=2)
file.close()

with open('my_json', 'r') as file:
    data1 = json.load(file)

print(data1)