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
arr1 = []
with open('decoder1.h', 'w') as file:
    file.write('direct = [ \n')
    for i in my_dict.values():
        if i != [0]:
            arr1.append(i[0])
            file.write(f'{i[0]}, \n')
            count += 1
        if count == 256:
            last = binary_to_decimal(i[0][2:])
            break
    file.write('];\n')
    file.write('\n')
    file.write('back = [ \n')
    arr2 = [0] * (last + 1)
    for i in range(last + 1):
        if arr1.count('0b'+bin(i).zfill(12)):
            arr2[i] = arr1.index('0b'+bin(i).zfill(12))
    for decimal in arr2:
        file.write(str(decimal) + ',' + '\n')
    file.write('];')
    file.close()

#000 -> 0b000000000001(001) -> 000
#255 -> 0b001011001011(715) -> 255