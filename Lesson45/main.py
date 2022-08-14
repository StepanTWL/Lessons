from Lesson45 import package1
from package1 import file1
from package1 import file2
from package1.file1 import c

print(file1.b)
print(file2.d)
print(c)

print(package1.a)#можно так писать после того как в __init__ добавили строки 