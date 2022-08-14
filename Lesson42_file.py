file = open('1.txt')
print(file.read(2))#Первые 2 символа
print(file.read(2))#Вторые 2 символа
file.seek(0)#возращение каретки в начало строки
print(file.readline())#выводит строку

file.seek(0)
for row in file:
    print(row)#будет печатать по строкам

file.seek(0)
for row in file:
    for letter in row:
        print(letter)#будет печатать по буквам

file.close()
file = open('1.txt', 'a')
file.write('\nlol')
file.close()