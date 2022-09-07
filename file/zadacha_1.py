f = open('1.txt', 'r')
s = f.readlines()
k = len(s)
i = 0
print(s)
print(k)
while int(i) < int(k):
    i +=1
    c = 0
    for p in s[i-1]:
        c += len(p.strip('\n'))
    print(f'В', i, 'строке,', c, 'букв')
f.close()