#Исключения Exceptions

print('hello1')
try:
    int('hello')
except ValueError:
    print('Yahoo')
try:
    [1,2][5]
except IndexError:#можно LookupError
    print('Yahoo')
print('hello3')


