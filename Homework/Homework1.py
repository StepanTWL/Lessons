f=open("bus_in.txt", "r")
a = int(f.read()) + 1
f.close()
f=open("bus_out.txt", "w")
f.write(str(a))
f.close()

f=open("bus_in.txt", "r")
S = int(f.read())
Petya = 0
Katya = 0
Sereja = 0
f.close()
f=open("bus_out.txt", "w")
Petya = Sereja = int(S / 6)
Katya = int((Sereja + Petya) * 2)
f.write(str(Petya)+' '+str(Katya)+' '+str(Sereja))
f.close()

f=open("INPUT.TXT", "r")
s = f.read().split()
f.close()
s1=[int(x) for x in s]
sum = s1[0]*3 + s1[1]*5 + s1[2]*12
f=open("OUTPUT.TXT", "w")
f.write(str(sum))
f.close()

#prodoljit' domashku s 8 uroke

n = 20
print(str(n-1)+'<'+str(n)+'<'+str(n+1))

a = 5
b = 4
print(str(a)+' * '+str(b)+' = '+str(a*b))

a = 46546874
print(str(a%10))


s3='afwr3afdsafg43'
print(s3[2])
print(s3[-2])
print(s3[:5])
print(s3[:-2])
print(s3[::2])
print(s3[1::2])
print(s3[::-1])
print(s3[::-2])
print(len(s3))

a = 5
b = 6
a, b = b, a
print(a, b)


f=open("INPUT.TXT", "r")
s = f.read().split()
f.close()
s1=[int(x) for x in s]
sum = s1[0]*s1[1]*s1[2]*2
f=open("OUTPUT.TXT", "w")
f.write(str(sum))
f.close()

hour = 1
minute = 35
second = 22
hour_ = 2
minute_ = 35
second_ = 21
h = m = s = 0
if (second_ >= second):
    s = second_ - second
else:
    s = 60 + second_ - second
    m = -1
if (minute_ + m >= minute):
    m += minute_ - minute
else:
    m += 60 + minute_ - minute
    h = -1
if (hour_ + h >= hour):
    h += hour_ - hour
else:
    h += 60 + hour_ - hour
sum = h*60*60 + m*60 + s
print(sum)
