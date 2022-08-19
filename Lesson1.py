from audioop import add


tple = ("first", 25, 25.1)
print(tple)
print(type(tple))
print(type(list((45, 1))))

dict = {"apple": "red", "banan": "yellow"}
print(dict)
print(type(dict))
for i in dict.items():
    print(i)
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)
dict["banan"] = "green"
print(dict["banan"])
del(dict["banan"])
dict["mango"] = "blue"
print(dict)


