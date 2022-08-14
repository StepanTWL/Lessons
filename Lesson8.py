#Regulyarnye vyrajeniya (shablon)

import re
from unittest import result

s = 'leklnfaklejn.fiowif3i20929.3urjlasnfla.skf0w3h4j]43.9jh]wpoej;amf.as:Lmf42-09tuj-2'
result = re.match('lekl', s)#poisk imenno v na4ale stroki
result1 = re.search('209', s)#poisk vezde do pervogo popavshego
result2 = re.findall('0', s)#nahodit vse i vydaet v vide massiva tipa ['0', '0', '0']
result3 = re.split('0', s)#po zadannomu znaku razbivaet stroku
result4 = re.sub('0', '!', s)#v stroke menyaet odin znak na drugoi
result5 = re.fullmatch('0', s)#sravnenie identi4nye li stroki
print(result)
print(result1)
print(result1[0])
print(result2)
print(result3)
print(result4)
print(result5)