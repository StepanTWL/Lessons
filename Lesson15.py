def square(a):
    print('Периметр кавадрата со стороной ' + str(a) + ' равен ' + str(4*a))
    print('Площадь кавадрата со стороной ' + str(a) + ' равна ' + str(a*a))

def square1(a):
    p = 4 * a
    s = a ** 2
    return p, s

square(5)

b = 10
print('Периметр кавадрата со стороной ' +str(b)+ ' равен ' + str((lambda a: 4 * a)(b)))

s1 = 10
s2 = 12
s3 = 18
print('Среднее арифметическое 3 чисел равно ' + str((lambda a, b, c: (a+b+c)/3)(s1, s2, s3)))


a = 3
b = 1
c = 5
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

year = 2304
if (year % 4 == 0 and year % 100) or (year % 400 == 0):
    print('Год '+ str(year) + ' высокосный')
else:
    print('Год '+ str(year) + ' не высокосный')

p = 1
for i in range(1, 101):
    if not i % 2:
        p *= i
print("Произведение четных чисел от 0 до 100 равно ", p)

t1 = 65468
t2 = 4654
t1_ = t1
t2_ = t2

while t1 and t2:
    if t1 > t2:
        t1 %= t2
    else:
        t2 %= t1

print("Наибольший общий делитель чисел ", t1_, " и ", t2_, "равен ", t1+t2)


w = 65431
def simple(a):
    for i in range(2, int(w/2 + 1)):
        if (not w % i):
            print("Число ", w, " не простое. Его делитель ", i)
            return
    print("Число ", w, " простое")

simple(w)


w1 = 1000
mass = []

for i in range(2, int(w1/2 + 1)):
    if (not w1 % i):
        mass.append(i)

if len(mass):
    print("Число ", w1, " не простое. Его делители ", mass)
else:
    print("Число ", w1, " простое")




w2 = 12345
w2_ = w2
s = 0

while w2 > 0:
    s += w2 % 10
    w2 //= 10

print("Сумма чисел числа ", w2_, " равна", s)



arr = [5, 55, 2, 75, 18, 8, 0, 31]
    
for i in range(len(arr)):
    arr[i] **= 2

print(arr)


arr1 = [5, 55, 2, 75, 18, 8, 0, 31]
arr2 = []

for i in arr1:
    arr2.append(i**2)

print(arr2)


arr3 = [5, 55, 2, 75, 18, 8, 0, 31]
arr4 = [x**2 for x in arr3]
print(arr4)

s5 = '024-24-02-ipajdf-a j-(J _(J(32-i-q0,qk:JKKLJ:KLJ:JJKNJN 9juJNBHU'
s6 = ''

for i in s5:
    if (i != ' ') and (i not in s6):
        s6 += i

print(s6)


s7 = ' 024-24-02-ipajdf-a j-(J _(J(32-i-q0,qk:JKKLJ:KLJ:JJKNJN 9juJNBHU '
print("Количество слов в фразе ", len(s7.split()))


s8 = '29.12.1983'
s9 = ''
s10 = 0
summ1 = 0

for i in s8:
    if i != '.':
        s9 += i

s10 = int(s9)
while s10 > 0:
    summ1 += s10 % 10
    s10 //= 10
summ1 = summ1 % 10 + summ1 // 10

print("Счастливое число ", summ1)