def look(*args):
    print(args)
    print(type(args))#kortej
    print(sum(args))

def brand(**args):
    print(args)
    print(type(args))#slovar'
    for x, y in args.items():
        print(x, ':', y)

look(1, 2, 3, 4)
brand(a='Apple', b='Samsung')