rub = 10
kop = 99
print(f"У меня есть {rub} рублей {kop} копеек \n"*3)

print('hello'.upper())
print('HELLO'.lower())
print('dk39jf09qjwq091jd'.count('9',10,30))
print('ske09iq-2ia-sdaskd'.find('!',1,10))
#print('ske09iq-2ia-sdaskd'.index('!',1,10)) v otli4ii ot find zakan4ivaetsya oshibkoi programmy esli ne nashlo
print('jnwe091j1092031'.replace('0','1',2))
print('ske09iq-2ia-sdaskd'.isalpha())#sostoit li tol'ko iz strok? .isdigit() toje samoe dlya cifr
print('111'.rjust(10, 'L'))#uveli4ivaet dlinu stroki do 10, zna4eniya prijimayutsya k pravo (ljust - toje samoe tol'ko vlevo)
print('jhgh jhggh kghkh'.split())
print('='.join(['1','2','3']))
print('   hello   \n'.strip())#udalyaet probel'nye znaki sprava i sleva (rstrip udolyzet tol'ko sprava, lstrip - sleva)
s=input().upper()#ru4noi vvod srazu preobrazuet i sohranyaet bol'shimi bukvami
print(type(s))