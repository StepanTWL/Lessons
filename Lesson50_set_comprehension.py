my_set = {i for i in range(1,6)}#{1,2,3,4,5}
my_set1 = {i for i in [1,1,2,2,3,4,5,5,5,]}#{1,2,3,4,5}
my_set2 = {i for i in 'sdfsfw3fdsdv'}#{'w', 'v', '3', 'd', 's', 'f'}
print(my_set2)

my_set3 = {i for i in ['hello', 'hi', 'qwerty'] if len(i)>4}#{'qwerty', 'hello'}
print(my_set3)
my_set4 = {i+j for i in 'abc' for j in 'def'}#{'af', 'bd', 'cf', 'ae', 'be', 'ce', 'bf', 'cd', 'ad'}
print(my_set4)
my_set5 = {(i,j) for i in 'abc' for j in 'def'}#{('a', 'e'), ('b', 'e'), ('c', 'd'), ('c', 'f'), ('c', 'e'), ('a', 'd'), ('b', 'd'), ('a', 'f'), ('b', 'f')}
print(my_set5)