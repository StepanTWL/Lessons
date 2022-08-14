f=open("dirc_in.txt", "r")
count = sum(1 for line in f)
f.seek(0)
arr = []
for i in range(count):
    arr.append([x for x in f.readline().split()])
f.close()
f=open("dirc_out.txt", "w")
for i in range(len(arr[0])):
    for j in range(len(arr[1])):
        f.write(arr[0][i]+arr[1][j]+'\n')
        f.write(arr[0][i]+arr[1][j]+'!'+'\n')
f.close()