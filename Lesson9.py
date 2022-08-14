#Regulyarnye vyrajeniya part 2

import re

s = "024-24-02-ipajdf-a j-(J _(J(32-i-q0,qk:JKKLJ:KLJ:JJKNJN 9juJNBHU"
result = re.search(r"K.L", s)#r - zna4aet syraya stroka (propuskayutsya spec simvoly tipa /n /t), . - odin lyuboi simvol
result1 = re.search(r"\d\d\d.\d\d", s)# \d - lyubuyu cifru, \D - lyuboi simvol, \s - probel'nyi simvol (konec stroki, tabulyaciya, probel)
result2 = re.search(r"[^A-J]", s)#is4etsya iz spiska ABCDEFJ, ^ - ne iz spiska
result3 = re.search(r"A|J", s)#is4etsya iz spiska ABCDEFJ, ^ - ne iz spiska
result1 = re.search(r"\d{2,3}.\d{1,2}", s)
print(result)
print(result1)
print(result2)
print(result3)


s1 = "Hello, i am fine. How are you?"
result4 = re.findall(r'\b[aeiouAEIOU]\w*', s1)
print(result4)