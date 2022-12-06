def test():
    return 'test'

print(f'test(): {test()}')

print(f'{"test".replace("tt", "t")}')

print(f'{test().replace("tt", "t")}')

text = (
    f'name: {100}',
    f'age: {25.0}'
)

name = 'Alex'
print(f'{name=}')#"name='Alex'"


def test1():
    return 'test_result'
print(f'{test1()=}')#"test1()='test_result'"


print(f'{20.1:.2f}')#'20.10'
print(f'{20.1:.5f}')#'20.10000'

value = 21.54
print(f'{value=:.1f}')#'21.5'


import datetime
now = datetime.datetime
print(f'{now.utcnow()=:"%d:%m:%y"}')#now.utcnow()="06:12:22"
print(f'{now.utcnow():"%d:%m:%y"}')#"06:12:22"


data = [("x", "y", "sum"), (1, 2, 3), (3, 5, 8)]
for x, y, sum in data:
    print(f"{x:1} {y:1} {sum:2}")
"""
x y sum
1 2  3
3 5  8
"""