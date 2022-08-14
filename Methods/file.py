#"r"- Чтение - Значение по умолчанию. Открывает файл для чтения, ошибка, если файл не существует    - default
#"a"- Append - открывает файл для добавления, создает файл, если он не существует
#"w"- Write - открывает файл для записи, создает файл, если он не существует
#"x"- Create - Создает указанный файл, возвращает ошибку, если файл существует
#"t"- Текст - значение по умолчанию. Текстовый режим                                                - default
#"b"- Двоичный - Двоичный режим (например, изображения)
#r+ означает чтение и запись файла. 
#w+ означает чтение и запись файла. 
#a+ означает чтение и запись файла, режим добавления.
f = open("demofile.txt", "wt+")


################# Close ################
f = open("demofile.txt", "r")
print(f.read())
f.close()


################ Fileon ################
f = open("demofile.txt", "r")
print(f.fileno())#Метод возвращает файловый дескриптор потока в виде числа. Если операторская система не использует файловый дескриптор, возникнет ошибка.


################# Flush ################
f = open("demofile.txt", "a")#Метод очищает внутренний буфер
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one! \n")#Now the file has one more line!...and another one!
f.write("Hello my friends \n")
f.write("How are you? \n")
f.close()


################ Isatty ################
f = open("demofile.txt", "r")#Метод возвращает True, если файловый поток является интерактивным, например: подключен к терминальному устройству.
print(f.isatty())#false
f.close()


################# Read #################
f = open("demofile.txt", "r")#Метод возвращает указанное количество байтов из файла. По умолчанию -1, что означает весь файл.
print(f.read())
print(f.read(33))
f.close()


############### Readable ###############
f = open("demofile.txt", "r")#Метод возвращает True, если файл доступен для чтения, и False, если нет.
print(f.readable())#true
f.close()


############### Readline ###############
f = open("demofile.txt", "r")#метод возвращает одну строку из файла
print(f.readline())
print(f.readline())
print(f.readline(5))#Вернуть только пять первых байтов из первой строки
f.close()


############### Readlines ##############
f = open("demofile.txt", "r")#метод возвращает список, содержащий каждую строку в файле как элемент списка.
print(f.readlines(133))#Используйте параметр hint, чтобы ограничить количество возвращаемых строк. Если общее количество возвращенных байтов превышает указанное число, строки больше не возвращаются.
f.close()


################# Seek #################
f = open("demofile.txt", "r")#Метод устанавливает текущую позицию файла в файловом потоке. метод также возвращает новую позицию
f.seek(4)#the file has one more line!...and another one! Now - не выдается.
print(f.readline())
f.close()


############### Seekable ###############
f = open("demofile.txt", "r")#Метод возвращает True, если файл доступен для поиска, и False, если нет.
print(f.seekable())#Файл доступен для поиска, если он разрешает доступ к файловому потоку, например метод seek().
f.close()


################# Tell #################
f = open("demofile.txt", "r")#Метод возвращает текущую позицию файла в файловом потоке.
print(f.tell())#Совет: Вы можете изменить текущую позицию в файле с помощью метода seek().
f.close()


############### Truncate ###############
f = open("demofile2.txt", "a")
f.truncate(20)#метод изменяет размер файла до заданного количества байтов
f.close()#Если размер не указан, будет использоваться текущая позиция.
#open and read the file after the truncate:
f = open("demofile2.txt", "r")
print(f.read())


############### Writable ###############
f = open("demofile.txt", "a")#Метод возвращает True, если файл доступен для записи, и False, если нет.
print(f.writable())#true


################# Write ################
f = open("demofile2.txt", "a")
f.write("See you soon!")#Метод записывает указанный текст в файл
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


############## Writelines ##############
f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])#Метод записывает элементы списка в файл
f.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())