class Cat:
    breed = 'pers'
    def hello():
        print("Hello!!!")
    
    def show_breed(self):
        print(f'My breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')
    
    def set_value(self, value, age=0):
        self.name = value
        self.age = age

walt = Cat()
walt.show_breed()#My breed is pers
walt.breed = 'siam'
walt.show_breed()#My breed is siam
walt.__dict__#{'breed': 'siam'}
bob = Cat()
bob.show_breed()#My breed is pers
mary = Cat()
mary.show_name()#nothing
mary.name = 'Kitty'
mary.show_name()#my name is Kitty
tom = Cat()
tom.set_value('Tom')
tom.show_name()#my name is Tom
jerry = Cat()
jerry.set_value('Jerry')#name: Jerry, age: 0
jerry.set_value('Jerry', 15)#name: Jerry, age: 15