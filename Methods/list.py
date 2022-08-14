#Элементы списка упорядочены, изменяемы и допускают дублирование значений.

################ Append ################
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)#Метод добавляет элемент в конец списка.
print(a)#['apple', 'banana', 'cherry', ["Ford", "BMW", "Volvo"]]


################# Clear ################
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()#Метод удаляет все элементы из списка
print(fruits)#[]


################# Copy #################
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()#метод возвращает копию указанного списка
print(x)#['apple', 'banana', 'cherry']


################# Count ################
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")#Метод возвращает количество элементов с указанным значением.
print(x)#1


################ Extend ################
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)#метод добавляет указанные элементы списка (или любые итерации - list, set, tuple, etc.) в конец текущего списка
print(fruits)#['apple', 'banana', 'cherry', 1, 4, 5, 9]


################# Index ################
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")#Метод возвращает позицию при первом появлении указанного значения. Если нет то ошибка
print(x)#2


################ Insert ################
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")#метод вставляет указанное значение в указанную позицию.
print(fruits)#['apple', 'orange', 'banana', 'cherry']


################# Pop ##################
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)#метод удаляет элемент в указанной позиции
print(fruits)#['apple', 'cherry']
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)#banana


################ Remove ################
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove("banana")#метод удаляет первое вхождение элемента с указанным значением. Если нет то ошибка
print(fruits)#['apple', 'cherry']


################ Reverse ###############
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()#Метод меняет порядок сортировки элементов на обратный.
print(fruits)#['cherry', 'banana', 'apple']


################# Sort #################
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()#метод сортирует список по возрастанию по умолчанию.
print(cars)#['BMW', 'Ford', 'Volvo']
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)#['Mitsubishi', 'Ford', 'BMW', 'VW']