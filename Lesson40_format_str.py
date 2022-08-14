name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

text = """Дорогой """ + name +' '+ mid_name + """, баланс вашего лицевого счета составляет """ + str(balance) + """ грн."""

text1 = """Дорогой {0} {1}, баланс вашего лицевого счета составляет {2} грн.""".format(name, mid_name, balance)
text2 = """Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} грн.""".format(name=name, mid_name=mid_name, balance=balance)
print(text1)


def f(x):
    return x*2


text3 = f"""Дорогой {name.lower()} {mid_name.upper()}, баланс вашего лицевого счета составляет {f(balance)} грн."""
print(text3)

d = {
    'name' : 'Семен',
    'mid_name' : 'Семенович',
    'balance' : 32.56,
}
text4 = f"""Дорогой {d['name']} {d['mid_name']}, баланс вашего лицевого счета составляет {d['balance']} грн."""
print(text4)


gender = {
    'm' : 'Дорогой',
    'f' : 'Дорогая',
}

a = [
    ["Семен", "Семенович", 32.56, "m"],
    ["Тамара", "Ивановна", 23.16, "f"],
    ["Павел", "Павлович", 3.26, "m"],
]

for name1, mid_name1, balance1, g in a:
    text5 = f"""{gender[g]} {name1} {mid_name1}, баланс вашего лицевого счета составляет {balance1} грн."""
    print(text5)