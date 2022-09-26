#Магические методы __getitem__, __setitem__, __delitem__

class Vector:

    def __init__(self, *args) -> None:
        self.values = list(args)

    def __repr__(self) -> str:
        return str(self.values)

    def __getitem__(self, item):#можно сделать и через ключи в словаре
        if 0<=item<len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границей')

    def __setitem__(self, key, value):
        if 0<=key<len(self.values):
            self.values[key] = value
        elif key>len(self.values):
            diff = key - len(self.values) + 1
            self.values.extend([0]*diff)
            self.values[key] = value
        else:
            raise IndexError('Индекс за границей')

    def __delitem__(self, key):
        if 0<=key<len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границей')
    
v1 = Vector(1,2,3,6456)
print(v1)#[1, 2, 3, 6456]
print(v1.values)#[1, 2, 3, 6456]
print(v1[3])#6456 
v1[3] = 645
print(v1[3])#645
del v1[3]
print(v1)#[1, 2, 3]
v1[5] = 645
print(v1)#[1, 2, 3, 0, 0, 645]
