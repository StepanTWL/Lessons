#Магические методы __item__, __next__

class Mark:

    def __init__(self, value) -> None:
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('marks')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter



class Student:

    def __init__(self, name, surname, marks) -> None:
        self.name = name
        self.surname = surname
        self.marks = marks
        self.index = 0

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        return iter(self.marks)

    def __next__(self):
        print('student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m= Mark([3,4,5,6,3])
igor = Student('Igor', 'Nikolaev', m)
print(next(igor))
for i in igor:
    print(i)

