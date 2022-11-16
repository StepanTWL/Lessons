def test():
    for i in range(3):
        yield i


a = test()
print(next(a))
print(next(a))
print(next(a))


def test1():
    for i in range(3):
        yield i


for i in test1():
    print(i)


def test2():
    yield  from [1, 2, 3]

for i in test2():
    print(i)


def test3():
    yield from [x for x in range(20)]


for i in test3():
    print(i)


def test4():
    print('start')
    while True:
        yield 1
        yield 2


a=test4()
print(next(a))#1
print(next(a))#2
print(next(a))#1


def test5():
    print('start')

    while True:
        x = yield
        print('recv:', x)

a = test5()
next(a)#recv: None
next(a)#recv: test
a.send('test')