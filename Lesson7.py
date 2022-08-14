#MNOJESTVO (SET)

numbers = {1, 2, 5, 9}
numbers1 = set()
numbers2 = set([1, 2, 1, 2, 5, 0]) #iz spiska delaem mnojestvo 4to by ubrat' dublikaty
numbers3 = {1, 2, 5, 8}
numbers4 = {1, 2, 5, 9}
numbers9 = frozenset({1, 2, 3})#nel'zya izmenyat'

numbers.add(55)
numbers.discard(58)#mojno ispol'zovat' dlya udaleniya elementa daje esli ego net
numbers.remove(1)#mojno ispol'zovat' dlya udaleniya elementa tol'ko esli on est' ina4e oshibku vydast
numbers.pop()#udalyaet 1 element
numbers.clear()#udalaet vse elementy
numbers5 = numbers3.union(numbers4) #numbers5 = numbers3 | numbers4
numbers6 = numbers3.intersection(numbers4) #numbers5 = numbers3 & numbers4
numbers7 = numbers3 - numbers4
numbers8 = numbers3.copy()

print(numbers)
print(type(numbers))
print(numbers2)

for i in numbers:
    print(i)

print (1 in numbers)
print(numbers5)
print(numbers6)
print(numbers7)
print(numbers8)
print(len(numbers8))
print(numbers9)