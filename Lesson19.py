a = 10
b = 8
if a>b:
    a,b=b,a
print(a,b)

#a,b = map(int, input.split()) esli danne vvodyatsya odnoi strokoi s probelom
a1 = 654445646
b1 = 548754
while a1>0 and b1>0:
    if (a1>b1):
        a1, b1 = b1, a1%b1
    else:
        a1, b1 = b1%a1, a1
if a1:
    print(a1)
else:
    print(b1)