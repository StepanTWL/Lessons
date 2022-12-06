def test1():
    i = 0
    value = 10_000_000
    while i <= value:
        i += 1


def test2():
    i = 0
    value = 10_000_000
    for _ in range(value):
        i += 1


test1()
test2() #быстрее