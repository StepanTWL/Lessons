def test(*args):
    print(args)


test(1, 2, 3, 4, 5)  # кортеж (1, 2, 3, 4, 5)
a = [1, 2, 3]
test(*a)  # кортеж (1, 2, 3)


def test1(*args, **kwargs):
    print(kwargs)


a = {'1': '1'}
test1(1, a)  # {} 1 и словарь идут в args
test1(1, **a)  # {'1': '1'} явно указано что словарь нужно засунуть в kwargs
