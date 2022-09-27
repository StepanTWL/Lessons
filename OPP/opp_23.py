#наследование Extending

class Person:
    
    def breathe(self):
        print('person breathe')

    def sleep(self):
        print('person sleep')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)

class Doctor(Person):
    age = 30
    def breathe(self):
        print('doctor breathe')

    def sleep(self):
        print('doctor sleep')
    
    def walk(self):
        print('doctor walk')

d=Doctor()
d.combo()#doctor breathe
        #doctor walk
        #doctor sleep
p=Person()
p.combo()#person breathe
        #person sleep
