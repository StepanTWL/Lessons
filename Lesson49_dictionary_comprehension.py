a = {i:i**2 for i in range(1,11)}#{1:1, ..., 10:100}
b = {word:len(word) for word in ['hello', 'hi', 'www']}#{'hello':5, ..., 'www':3}

data = {
    'Jeff BezoS': '177',
    'ilon MaSk': '126',
}

new_data = {key.title(): int(value) for key, value in data.items()}#{'Jeff Bezos': 177, 'Ilon Mask': 126}

users = [
    [0, 'Bob', 'password'],
    [2, 'code', 'python'],
    [22, 'qwerty', '1234'],
]

new_users = {user[0]: user for user in users}#{0: [0, 'Bob', 'password'], 2: [2, 'code', 'python'], 22: [22, 'qwerty', '1234']}
print(new_users[22])#[22, 'qwerty', '1234']

