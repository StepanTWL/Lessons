class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f"instance_hello {self}")
    
    @staticmethod #анпример если нужна функция которую не нужно реализовать внутри класса
    def static_hello():
        print('static_hello')

    @classmethod #если нужна обработка не над экземплярами а над целым классом
    def class_hello(cls):
        print(f"class_hello {cls}")


Example.hello()
#Example.instance_hello() ошибка
Example.static_hello()
Example.class_hello()#class_hello <class '__main__.Example'>
a=Example()#экземпляр
#a.hello() ошибка
a.instance_hello()#метод      instance_hello <__main__.Example object at 0x00000000039CE9D0>
a.static_hello()
a.class_hello()#class_hello <class '__main__.Example'>