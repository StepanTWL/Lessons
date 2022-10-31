
arr=[]
with open('dirc_in.txt', 'r') as file:
    for line in file:
        if len(line)>1:
            arr.append(line[:-1])
        else:
            arr.append(line)
    file.close()

with open('dirc_out.txt', 'w') as file:
    for first in arr:
        file.write(first+'\n')
        if first[0].isalnum():
            file.write(first[0].upper()+first[1:]+'\n')
        for second in arr:
            file.write(first+second+'\n')
            if first[0].isalnum():
                file.write(first[0].upper()+first[1:]+second+'\n')
            for third in arr:
                file.write(first+second+third+'\n')
                if first[0].isalnum():
                    file.write(first[0].upper()+first[1:]+second+third+'\n')
    file.close()