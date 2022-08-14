#Spiski (list)

s = ['hi', True, 2, 3, 4]
print(len([1,2,3]+[5]*5))

print(3 in s)

s1 = [43, 53, 32, 1, 434, 12, 1, -1, 5.3, 22.2]
print(min(s1))
print(sum(s1))
print(sorted(s1, reverse=True))
print(sum(s1)/len(s1))#srednee
print(s1[::2])
print(s1[::-1])
s2=s1#sohranyaet sylku na ob'ekt spiska
s2[0] = 0
print(s1)
s2=s1[:]#sohranyaet dublikat spiska
s2=s1.copy()#toje samoe 4to i vyshe
s2[1] = 0
print(s1)
s2.clear()
print(s2)
s1.insert(0, 100)#dob v lyuboe mesto
print(s1)
print(s1.pop(5))#udalayet element na meste 5 i vydaet ego
print(s1)
s1.remove(-1)#udalayet element -1
print(s1)
s1.sort(reverse=True)
print(s1)