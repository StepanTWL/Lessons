#Все строковые методы возвращают новые значения. Они не изменяют исходную строку.
#Вы можете назначить многострочную строку переменной, используя три кавычки

txt = "The best things in life are free!"
print("free" in txt)#True

############## Capitalize ##############
txt = "pytHOn is FUN!"
x = txt.capitalize()#возвращает строку, в которой первый символ в верхнем регистре, а остальные в нижнем регистре
print (x)#Python is fun!


############### Casefold ###############
txt = "Hello, AnD Welcome To My World!"
x = txt.casefold()#возвращает строку, в которой все символы в нижнем регистре
print(x)#hello, and welcome to my world!


################ Center ################
txt = "banana"
x = txt.center(20, '+')#выровняет строку по центру, используя указанный символ (пробел по умолчанию) в качестве символа заполнения
print(x)#+++++++banana+++++++


################# Count ################
txt = "I love apples, apple are my favorite fruit"
x = txt.count("p", 5, 30)#Метод возвращает количество раз, когда указанное значение появляется в строке, сожно указать диапазон поиска
print(x)#4
x = txt.count("q")
print(x)#0 (не встречается)


################# Encode ###############
txt = "My name is Ståle"
x = txt.encode()#метод кодирует строку, используя указанную кодировку. Если кодировка не указана, будет использоваться UTF-8.
print(x)#b'My name is St\xc3\xe5le'
print(txt.encode(encoding="ascii",errors="backslashreplace"))#использует обратную косую черту вместо символа, который не может быть закодирован     b'My name is St\\xe5le'
print(txt.encode(encoding="ascii",errors="ignore"))#игнорирует символы, которые не могут быть закодированы                                          b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))#заменяет символ текстом, объясняющим символ                                                b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
#print(txt.encode(encoding="ascii",errors="strict"))#По умолчанию, выдает ошибку при сбое                                                            сбой
print(txt.encode(encoding="ascii",errors="replace"))#заменяет символ вопросительным знаком                                                          b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))#заменяет символ символом xml                                                         b'My name is Ståle'


############### Endswith ###############
txt = "Hello, welcome to my world."
x = txt.endswith(".")#метод возвращает True, если строка заканчивается указанным значением, иначе False.
print(x)#True
x = txt.endswith(",", 2, 6)
print(x)#True


############## Expandtabs ##############
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)#метод устанавливает размер табуляции на указанное количество пробелов
print(x)#H e l l o


################# Find #################
txt = "Hello, welcome to my world."
x = txt.find("welcome")#Метод находит первое вхождение указанного значения
print(x)#7
x = txt.find("1", 3, 8)#поиск от 3 до 7 вкл. знака
print(x)#-1 (нет)


################ Format ################
txt = "For only {price:.2f} dollars!"#метод форматирует указанные значения и вставляет их в заполнитель строки
print(txt.format(price = 49))#For only 49.00 dollars!
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)#My name is John, I'm 36
txt2 = "My name is {0}, I'm {1}".format("John",36)#My name is John, I'm 36
txt3 = "My name is {}, I'm {}".format("John",36)#My name is John, I'm 36
txt = "We have {:<8} chickens."
print(txt.format(49))#We have 49       chickens.
"""
:<		Выравнивает результат по левому краю (в доступном пространстве)
:>		Выравнивает результат по правому краю (в доступном пространстве)
:^		Центр выравнивает результат (в доступном пространстве)
:=		Помещает знак в крайнее левое положение
:+		Используйте знак плюс, чтобы указать, является ли результат положительным или отрицательным.
:-		Используйте знак минус только для отрицательных значений
: 		Используйте пробел, чтобы вставить дополнительный пробел перед положительными числами (и знак минус перед отрицательными числами)
:,		Используйте запятую в качестве разделителя 
:_		Используйте подчеркивание в качестве разделителя 
:b		Двоичный формат
:c		Преобразует значение в соответствующий символ Юникода.
:d		Десятичный формат
:e		Научный формат, со строчной буквой e
:E		Научный формат, с заглавной буквой E
:f		Исправить формат номера точки
:F		Фиксированный формат номера точки в верхнем регистре (показывать inf и nan как INF и NAN)
:g		Общий формат
:G		Общий формат (с использованием заглавной буквы E для научных обозначений)
:o		Восьмеричный формат
:x		Шестнадцатеричный формат, нижний регистр
:X		Шестнадцатеричный формат, верхний регистр
:n		Формат номера
:%		Процентный формат
"""


############## Format_map ##############
point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))#Метод format_map() аналогичен методу str.format(**mapping), за исключением того, что str.format(**mapping) создает новый словарь, а str.format_map(mapping) — нет.
print('{x} {y}'.format_map(point))#format_map(mapping) является более гибким, чем format(**mapping), так как у вас могут отсутствовать ключи.
#4 -5
class Coordinate(dict):
    def __missing__(self, key):
      return key
print('({x}, {y})'.format_map(Coordinate(x='6')))#(6, y)
print('({x}, {y})'.format_map(Coordinate(y='5')))#(x, 5)
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))#(6, 5)


################# Index ################
txt = "Hello, welcome to my world."
x = txt.index("welcome")#находит первое вхождение указанного значения
print(x)#метод вызывает исключение, если значение не найдено. (в отличи от .find который возращает -1)
print(txt.index("l", 2, 15))#2


################ Isalnum ###############
txt = "Company12"
x = txt.isalnum()#Метод возвращает True, если все символы являются буквенно-цифровыми, то есть буквами алфавита (a-z, A-Z) и цифрами (0-9).
print(x)#true


################ Isalpha ###############
txt = "Company1X"
x = txt.isalpha()#метод возвращает True, если все символы являются буквами алфавита (a-z, A-Z).
print(x)#False


################ Isascii ###############
txt = "~Company123"
x = txt.isascii()#метод возвращает True, если все символы являются символами ascii.
print(x)#true


############### Isdecimal ##############
txt = "\u0033" #unicode for 3
x = txt.isdecimal()#Метод возвращает True, если все символы являются десятичными (0-9). Только десятичные числа
print(x)#true


################ Isdigit ###############
txt = "\u00B2"#unicode for ²
x = txt.isdigit()#Метод возвращает True, если все символы являются цифрами, иначе False Десятичные числа, нижние индексы, верхние индексы
print(x)#true


############# Isidentifier #############
txt = "Demo"
x = txt.isidentifier()#Метод возвращает True, если строка является допустимым идентификатором (a-z, A-Z, 0-9, _), в противном случае — False.
print(x)#true


################ Islower ###############
txt = "hello world!"
x = txt.islower()#метод возвращает True, если все символы в нижнем регистре, иначе False.
print(x)#true


############### Isnumeric ##############
txt = "\u00BC"#¼
x = txt.isnumeric()#Метод возвращает True, если все символы являются числовыми (0-9), в противном случае — False. Десятичные дроби, нижние индексы, верхние индексы, обычные дроби, римские цифры, числители денежных единиц
print(x)#true


############## Isprintable #############
txt = "Hello!\nAre you #1?"
x = txt.isprintable()#Метод возвращает True, если все символы можно распечатать, иначе False.
print(x)#false


############### Isspace ################
txt = "   "
x = txt.isspace()#метод возвращает True, если все символы в строке являются пробелами, иначе False.
print(x)#true


############### Istitle ################
txt = "Hello, And Welcome To My World!"
x = txt.istitle()#Метод возвращает True, если все слова в тексте начинаются с прописной буквы, а остальная часть слова — строчными буквами, в противном случае — False.
print(x)#true
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())#False
print(b.istitle())#true
print(c.istitle())#true
print(d.istitle())#true


############### Isupper ################
txt = "THIS IS NOW!"
x = txt.isupper()#Метод возвращает True, если все символы в верхнем регистре, иначе False.
print(x)#true


################# Join #################
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)#метод принимает все элементы в итерируемом объекте и объединяет их в одну строку.
print(x)#John#Peter#Vicky
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)#nameTESTcountry


################# Ljust ################
txt = "banana"
x = txt.ljust(20, '+')#метод выровняет строку по левому краю, используя указанный символ (пробел по умолчанию) в качестве символа заполнения
print(x, "is my favorite fruit.")#banana++++++++++++++ is my favorite fruit.


################# Lower ################
txt = "Hello my FRIENDS"
x = txt.lower()#Метод возвращает строку, в которой все символы в нижнем регистре.
print(x)#hello my friends


################ Lstrip ################
txt = "     banana     "
x = txt.lstrip('.')#метод удаляет все начальные символы (пробел является начальным символом по умолчанию для удаления)
print("of all fruits", x, "is my favorite")#of all fruits banana     is my favorite
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip("saw,.")
print(x)#banan


############## Maketrans ###############
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")#метод возвращает таблицу сопоставления, которую можно использовать с методом translate() для замены указанных символов.
print(txt.translate(mytable))#Hello Pam!
txt = "Good night Sam!"
x = "mSa"#кого менять
y = "eJo"#на что менять
z = "odnght"#что исключить
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))#G i Joe!
print(txt.maketrans(x, y, z))#{97: 111, 83: 74, 100: None, 103: None, 104: None, 116: None, 109: 101, 110: None, 111: None}


############### Partition ##############
txt = "I could eat bananas all day"
x = txt.partition("bananas")#Метод ищет указанную строку и разбивает строку на кортеж, содержащий три элемента.
#Первый элемент содержит часть перед указанной строкой
#Второй элемент содержит указанную строку
#Третий элемент содержит часть после строки
print(x)#('I could eat ', 'bananas', ' all day')
x = txt.partition("apples")#
print(x)#('I could eat bananas all day', '', '')


################ Replace ###############
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)#метод заменяет указанную фразу другой указанной фразой.(2 - количество замен, без указания меняются все)
print(x)#three three was a race horse, two two was one too.


################# Rfind ################
txt = "Mi casa, su casa."
x = txt.rfind("casa",5,30)#метод находит последнее вхождение указанного значения или -1 если нет.
print(x)#12


################ Rindex ################
txt = "Mi casa, su casa."
x = txt.rindex("casa",5,30)#метод находит последнее вхождение указанного значения или ошибка если нет.
print(x)


################# Rjust ################
txt = "banana"
x = txt.rjust(20,'+')#метод выровняет строку по правому краю, используя указанный символ (пробел по умолчанию) в качестве символа заполнения.
print(x, "is my favorite fruit.")#++++++++++++++banana is my favorite fruit.


############## Rpartition ##############
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")#метод ищет последнее вхождение указанной строки и разбивает строку на кортеж, содержащий три элемента
print(x)#('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')


################ Rsplit ################
txt = "apple, banana, cherry"
x = txt.rsplit(", ")#Метод разбивает строку на список, начиная справа. Без max метод работает как split
print(x)#['apple', 'banana', 'cherry']
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)#['apple, banana', 'cherry']


################ Rstrip ################
txt = "     banana     "
x = txt.rstrip()#метод удаляет любые конечные символы (символы в конце строки), пробел является удаляемым завершающим символом по умолчанию
print("of all fruits", x, "is my favorite")#of all fruits     banana is my favorite
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)#banana


################# Split ################
txt = "apple, banana, cherry"
x = txt.rsplit(", ")#Метод разбивает строку на список, начиная слева. Без max метод работает как split
print(x)#['apple', 'banana', 'cherry']
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)#['apple', 'banana, cherry']


############## Splitlines ##############
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()#Метод разбивает строку на список. Разбиение выполняется на разрывах строк
print(x)#['Thank you for the music', 'Welcome to the jungle']
x = txt.splitlines(True)#По желанию. Указывает, следует ли включать разрывы строк (True) или нет (False). Значение по умолчанию — Ложь.
print(x)#['Thank you for the music\n', 'Welcome to the jungle']


############## Startswith ##############
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)#Метод возвращает True, если строка начинается с указанного значения, в противном случае — False.
print(x)#True


################ Strip #################
txt = "     banana     "
x = txt.strip()#метод удаляет все начальные (пробелы в начале) и конечные (пробелы в конце) символы (пробел — это удаляемый начальный символ по умолчанию)
print("of all fruits", x, "is my favorite")#of all fruits banana is my favorite
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)#banana


############### Swapcase ###############
txt = "Hello My Name Is PETER"
x = txt.swapcase()#метод возвращает строку, в которой все буквы верхнего регистра являются строчными и наоборот.
print(x)#hELLO mY nAME iS peter


################ Title #################
txt = "Welcome to my world"
x = txt.title()#Метод возвращает строку, в которой первый символ в каждом слове является прописным. Как заголовок или заголовок.
print(x)#Welcome To My World
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)#Hello B2B2B2 And 3G3G3G


############### Translate ##############
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
#Если вы используете словарь, вы должны использовать коды ascii вместо символов.
mydict = {83:  80}
txt = "Hello Sam!"#метод возвращает строку, в которой некоторые указанные символы заменены символом, описанным в словаре или в таблице сопоставления.
print(txt.translate(mydict))#Hello Pam!


################ Upper #################
txt = "Hello my friends"
x = txt.upper()#Метод возвращает строку, в которой все символы в верхнем регистре.
print(x)#HELLO MY FRIENDS


################ Zfill #################
txt = "50"
x = txt.zfill(10)#Метод добавляет нули (0) в начало строки, пока она не достигнет указанной длины
print(x)#0000000050