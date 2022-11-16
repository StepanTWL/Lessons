# Проврека запущена ли программа на прямую или она импортирована в модуль

def test(x, y):
    return x + y


if __name__ == '__main__':
    res = test(1, 2)
    print(f"test: {res} | __name__: {__name__}")
