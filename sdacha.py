s = input()
s = list(s)
for i in range(len(s)):
    if i % 3 == 0:
        s[i] = ''
s = ''.join(s)
print(s)