def offset(s: str, n: int) -> str:
    a = '0b' + s[n:] + s[:n]
    return a


def binary_to_decimal(n: str) -> int:
    n = int(n)
    a = 0
    count = 0
    while n > 0:
        if n % 10:
            a += 2 ** count
        count += 1
        n //= 10
    return a


my_dict = dict()
for i in range(1, 4095):
    my_dict[i] = []
    for j in range(12):
        my_dict[i].append(offset(bin(i)[2:].zfill(12), j))
suc = 0
for i in range(1, len(my_dict)):
    for j in range(i + 1, len(my_dict) + 1):
        for k in range(len(my_dict[i])):
            if my_dict[i][k] in my_dict[j]:
                suc = 1
                break
        if suc:
            my_dict[j] = [0]
            suc = 0
pass

count = 0
count_table = 0
count_one = 0
arr1 = []
with open('decoder1.h', 'w') as file:
    file.write('direct = [ \n')
    for i in my_dict.values():
        if i != [0]:
            count_table += 1
            arr1.append(i[0])
            if not count_table % 7:
                file.write(f' {i[0].rjust(15)}, \n')
            else:
                file.write(f' {i[0].rjust(15)},')
            count += 1
        if count == 1256:
            last = binary_to_decimal(i[0][2:])
            break
    file.write('];\n')
    file.write('\n')
    file.write('back = [ \n')

    """
    for i in arr1:
        if i.count('1') == 7:
            print(binary_to_decimal(i[2:]))
    """

    arr2 = [-1] * 4096
    for i in range(4096):
        for j in range(1, len(my_dict)):
            if my_dict[j] != [0]:
                for k in range(len(my_dict[j])):
                    if ('0b' + bin(i)[2:].zfill(12)) == my_dict[j][k]:
                        arr2[i] = arr1.index('0b' + bin(j)[2:].zfill(12))
    count_table = 0
    for decimal in arr2:
        count_table += 1
        if not count_table % 20:
            file.write(f' {str(decimal).rjust(4)}, \n')
        else:
            file.write(f' {str(decimal).rjust(4)},')
    file.write('];')
    file.close()
print(count_one)
