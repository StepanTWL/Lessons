import pickle # запись сложных объектов в файл
import sys
import time

print(time.asctime())#Wed Dec 28 16:44:41 2022
print(time.localtime())#time.struct_time(tm_year=2022, tm_mon=12, tm_mday=28, tm_hour=16, tm_min=45, tm_sec=30, tm_wday=2, tm_yday=362, tm_isdst=0)
print(sys.version)#3.8.10
for i in range(1, 3):
    print(i)
    time.sleep(1)

game = {"life":5, "lvl":2}
with open('test.txt', 'wb') as file:#битовая запись
    pickle.dump(game, file)

with open('test.txt', 'rb') as file:
    print(pickle.load(file))#{"life":5, "lvl":2}

