"""
english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for index, word in enumerate(english_words,1):
    print(f'Word № {index} = {word}')
"""

arr=[int(a) for a in input()]
sett=set(enumerate(arr,1))
arr1=[]
for i in range(1,len(sett)+1):
    if i%2:
        arr1.append(sett[i-1][1])
    elif not i%2:
        arr1.append(a if sett[i-1][1]*2>9 )
print(sett)