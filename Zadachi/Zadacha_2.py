#Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
a = [1, 3, 4, 6, 2, 5, 23, 45, 46]
b = [3, 56, 23, 4, 12, 31, 5, 45, 65]
c = a + b
c.sort()
d = 0
for i in c:
    if c.count(i) >= 2:
        d +=1
    else:
        continue
print(a)
print(b)
print(c)
print(f'В списках', d, 'одинаковых чисел')
