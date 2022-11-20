def offset(s: str, n: int) -> str:
    a = s[n:] + s[:n]
    return a


dictt = dict()
for i in range(1, 4095):
    dictt[i] = []
    for j in range(12):
        dictt[i].append(offset(bin(i)[2:].zfill(12), j))
suc = 0
for i in range(1, len(dictt)):
    for j in range(i + 1, len(dictt) + 1):
        for k in range(len(dictt[i])):
            if dictt[i][k] in dictt[j]:
                suc = 1
                break
        if suc:
            dictt[j] = [0]
            suc = 0
count = 0
with open('decoder1.h', 'w') as file:
    file.write('map <string, string> book = { \n')
    for i in dictt.values():
        if i != [0]:
            file.write(
            count += 1
        if count == 256:
            break
    file.write('};\n')