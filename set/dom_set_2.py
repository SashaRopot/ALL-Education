#Проверить, есть ли в последовательности чисел списка дубликаты
b = (1, 3, 16, 4, 2, 6, 5)
c = set(b)
print(c)
print(len(b))
print(len(c))
if len(b) > len(c):
    print('в списке есть дубликаты')
else:
    print('В списке нет дубликатов')