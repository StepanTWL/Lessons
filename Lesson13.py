s = [i ** 3 for i in range(1, 21) if i % 5 == 0]
print(s)
print(sum(s))

s1 = [(i, j) for i in range(1, 21) for j in range(1, 51)]
print(s1)

s2 = [i ** 2 if i > 0 else i ** 3 for i in range(-10, 11) if i % 2 == 0]
print(s2)

s3 = [1, 1, 3, 5, 5, 7]
set_set = {i for i in s3}
print(set_set)
dictionary = {i: i ** 10 for i in s3}
print(dictionary)