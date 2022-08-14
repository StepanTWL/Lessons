with open('1.txt', 'w') as file:
    file.write('123')
    file.write('hello')#<- после этого файл закрывается

import os

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')#.git -> 0 bytes И остальное что в папке находится

with os.scandir('..') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')#Lessons -> 0 bytes И остальное что находится в папке выше


import threading
balance_lock = threading.Lock()

with balance_lock:#позволяет не использовать balance_lock.acquire() - поставить блокировку, balance_lock.release() - снять блокировку само все сделает 
    pass