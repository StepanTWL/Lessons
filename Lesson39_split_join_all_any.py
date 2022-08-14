s = 'aaa'
s.split('a')#['','','','']

s1 = [50,60,70]
''.join([str(i) for i in s1])#506070

a = ['hello', 'world', 'hi']
all(a)#True
a1 = ['hello', '', 'hi']
all(a1)#false
any(a1)#true
a2 = ['', '']
any(a2)#false