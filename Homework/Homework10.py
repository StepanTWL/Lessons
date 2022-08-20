"""
english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for index, word in enumerate(english_words,1):
    print(f'Word № {index} = {word}')


arr=list(enumerate([int(a) for a in input()],1))
arr1=[]
for i in range(len(arr)):
    if not i%2:
        if arr[i][1]*2 > 9:
            arr1.append(arr[i][1]*2-9)
        else:
            arr1.append(arr[i][1]*2)
    else:
        arr1.append(arr[i][1])


a=sum(arr1)
a%=10
if sum(arr1)%10:
    print('False')
else:
    print('True')



def keanu_reeves() ->str:
    return print(f"YOU'RE BREATHTAKING")
keanu_reeves()



def summa_n(t:int) -> str:
    S=sum(range(t+1))
    return print(f"Я знаю, что сумма чисел от 1 до {t} равна {S}")

summa_n(5)




def check_password(s:str) -> str:
    count=0
    if len(s)<10:
        return print('Easy peasy')
    if s.islower():
        return print('Easy peasy')
    for i in s:
        if i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='*' or i.isalnum():
            continue
        else:
            return print('Easy peasy')
    for i in s:
        if i.isdecimal():
            count += 1
    if count<3:
        return print('Easy peasy')
    else:
        return print('Perfect password')

check_password(input())
"""

def count_letters(s:str) -> str:
    N=0
    K=0
    for i in s:
        if i.islower():
            K+=1
        elif i.isalpha():
            N+=1
    return print(f"Количество заглавных символов: {N}\nКоличество строчных символов: {K}")