# 1-----------------------
name = 'Test'
age = 17
print(f'Name: {name}, age {age}')


# 2-----------------------
with open('file.txt', 'w') as file:
    file.write('hello')

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 4444))
    s.sendall(b'data')


# 3-----------------------
try:
    value = 'hello'
    result = int(value)
except ValueError:  # пользователь наживает ctrl+c
    print('Value Error')  # вызывается KeyboardInterrupt
    # а не ValueError


# 4-----------------------
def test(value, arr=None):
    if arr is None:
        arr = []
    arr.append(value)
    return arr


l1 = test(0)  # [0]
l2 = test(1)  # [1]


def test2(value, arr=[]):
    arr.append(value)
    return arr


l3 = test(0)  # [0]
l4 = test(1)  # [0,1]


# 5-----------------------
from collections import namedtuple

ntuple = namedtuple('ntuple', ['x', 'y'])
n = ntuple(1, 2)

if isinstance(n, tuple);
    print('tuple')

a = None
if a is None:
    print('a is None')


# 6-----------------------
def check_bool_len(value: bool):
    if value:
        pass


# 7-----------------------
#print('what happen')
from loguru import logger
logger.debug('what happen!')