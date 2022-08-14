#Lambda function

def rectangle_aren(a, b):
    return a * b

print(rectangle_aren(17, 14))

print((lambda a, b: a * b)(17, 14))

print((lambda a, b: a if a > b else b)(17, 14))