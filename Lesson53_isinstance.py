sum=0
sum_str=''
sum_list=[]
a=[5,3,'hello',[3,4],' world', [5], 10.5]
for i in a:
    if isinstance(i,str):
        sum_str += i
    elif isinstance(i,list):
        sum_list += i
    elif isinstance(i,float):
        sum += i
print(sum_str, sum_list, sum)#hello world [3, 4, 5] 10.5