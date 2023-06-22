from copy import copy

arr = [1, 1, 2, 1, 1, 2, 2, 1]
arr_result = {}
dict_key = 0
dict_value = {
    'start': None,
    'stop': None,
}

for i in range(len(arr) - 2):
    if (arr[i] == 1 and arr[i + 1] == 2 and arr[i + 2] == 1) or (arr[i] == 2 and arr[i + 1] == 1 and arr[i + 2] == 2):
        arr[i + 1] = 0
if arr[0] != 0 and arr[0] != arr[1]:
    arr[0] = 0
if arr[-1] != 0 and arr[-1] != arr[-2]:
    arr[-1] = 0

print(arr)

for i in range(len(arr) - 1):
    if (arr[i] == 1 and arr[i + 1] == 1) or (arr[i] == 2 and arr[i + 1] == 2):
        if dict_value['start'] is None:
            dict_value['start'] = i
        dict_value['stop'] = i + 1
        arr_result[dict_key] = copy(dict_value)
    else:
        if dict_key in arr_result:
            dict_key += 1
            dict_value['start'] = None
            dict_value['stop'] = None

for i in range(len(arr_result)):
    print(arr_result[i])
print(arr)
