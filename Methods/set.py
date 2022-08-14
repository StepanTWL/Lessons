#Наборы используются для хранения нескольких элементов в одной переменной
#Набор — это коллекция, которая является неупорядоченной , неизменной (Элементы набора нельзя изменить, но вы можете удалять элементы и добавлять новые элементы.) и неиндексированной 


################# ADD ##################
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")#Метод добавляет элемент в набор.
print(fruits)#{'banana', 'orange', 'apple', 'cherry'}
thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
print(thisset)#{'banana', 'apple', 'cherry'}


################ Clear #################
fruits = {"apple", "banana", "cherry"}
fruits.clear()#метод удаляет все элементы в наборе
print(fruits)#set()


################# Copy #################
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()#метод копирует набор
print(x)#{'banana', 'cherry', 'apple'}


############## Difference ##############
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)#Метод возвращает набор, содержащий разницу между двумя наборами. Возвращаемый набор содержит элементы, которые существуют только в первом наборе, а не в обоих наборах.
print(z)#{'cherry', 'banana'}


########### Difference_update ##########
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)#Метод удаляет элементы, существующие в обоих наборах.
print(x)#{'cherry', 'banana'}


################ Discard ###############
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")#метод удаляет указанный элемент из набора. В отличии от remove при отсуствии нет ошибки
print(fruits)#{'cherry', 'apple'}


############# Intersection #############
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)#Метод возвращает набор, который содержит сходство между двумя или более наборами
print(z)#{'apple'}


########## Intersection_update #########
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)#Метод удаляет элементы, которых нет в обоих наборах (или во всех наборах, если сравнение выполняется между более чем двумя наборами).
print(x)#{'apple'}
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)#{'c'}


############## Isdisjoint ##############
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)#метод возвращает True, если ни один из элементов не присутствует в обоих наборах, в противном случае он возвращает False.
print(z)#True


############### Issubset ###############
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)#метод возвращает True, если все элементы набора существуют в указанном наборе, в противном случае он возвращает False.
print(z)#True


############## Issuperset ##############
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)#Метод возвращает True, если все элементы указанного набора существуют в исходном наборе, в противном случае он возвращает False.
print(z)#True


################## Pop #################
fruits = {"apple", "banana", "cherry"}
fruits.pop()#Метод удаляет случайный элемент из набора.
print(fruits)#{'banana', 'apple'}


################ Remove ################
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")#метод удаляет указанный элемент из набора. В отличии от discard при отсуствии будет ошибка
print(fruits)#{'cherry', 'apple'}


######### Symmetric_difference #########
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)#Метод возвращает набор, содержащий все элементы из обоих наборов, но не элементы, присутствующие в обоих наборах.
print(z)#{'cherry', 'google', 'banana', 'microsoft'}


###### Symmetric_difference_update #####
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)#метод обновляет исходный набор, удаляя элементы, присутствующие в обоих наборах, и вставляя другие элементы.
print(x)#{'cherry', 'microsoft', 'banana', 'google'}


################# Union ################
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)#метод возвращает набор, который содержит все элементы из исходного набора и все элементы из указанных наборов. Это не обязательно должен быть набор, это может быть любой итерируемый объект.
print(z)#{'microsoft', 'cherry', 'google', 'banana', 'apple'}
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)#{'b', 'f', 'a', 'e', 'c', 'd'}


################ Update ################
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)#метод обновляет текущий набор, добавляя элементы из другого набора (или любого другого итерируемого).
print(x)#{'apple', 'cherry', 'banana', 'microsoft', 'google'}