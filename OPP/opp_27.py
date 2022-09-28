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
try:
    1/0
except: #аналогично except BaseException:
    print('Zero error')
finally:
    print('end')
try:
    1/1
except: #аналогично except BaseException:
    print('Zero error')
finally:
    print('end1')
print('hello3')

"""
f = open('123.txt')
try:
    execute(f)
finally:
    print('end')
    f.close()
"""

try:
    {}['k']
except (KeyError, IndexError) as error:
    print("LookupError")
    print(f'Logging error: {error} {repr(error)}')#Logging error: 'k' KeyError('k')
except ZeroDivisionError as err:
    print('ZeroDivisionError')
    print(f'Logging error: {err} {repr(err)}')#Logging error: division by zero ZeroDivisionError('division by zero')
else:
    print('all good')
finally:
    print('end')


