from collections import Counter, deque
from queue import LifoQueue, PriorityQueue

numbers = [
    1, 2, 3, 4, 1, 2, 3, 4, 5, 123, 3, 2, 5, 6, 5, 4,
]

#быстрый подсчет топ значений
c = Counter(numbers)
res = c.most_common(3) # top3
print(res) # [(2, 3), (3, 3), (4, 3)]


#список с фиксированным значением элементов
a = deque(maxlen=3)
a.append(1)
a.append(2)
a.append(3)
print(a) # deque([1, 2, 3], maxlen=3)
a.append(4)
print(a) # deque([2, 3, 4], maxlen=3)
a.pop()
print(a) # deque([2, 3], maxlen=3)
a.popleft()
print(a) # deque([3], maxlen=3)
a.appendleft(5)


#реализация стека
b = LifoQueue(maxsize=3)
b.put(1)
b.put(2)
b.put(3)
print(b.queue)#[1, 2, 3]
print(b.get())#3
print(b.queue)#[1, 2]

#приоритетная очередь
d = PriorityQueue(maxsize=3)
d.put((1, 'task1'))
d.put((10, 'task2'))
d.put((4, 'task3'))

print(d.get())#(1, 'task1')
print(d.get())#(4, 'task3')
print(d.get())#(10, 'task2')