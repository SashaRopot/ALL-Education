#Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном
# с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего
# букв в слове, сколько гласных и согласных.
a = input('Введите произвольное слово: ')
b = 'аоуэыяёюеиАОУЭЫЯЁЮЕИ'
c = 0
d = 0
k1 = 0
k2 = 0
k = len(a)
for i in range(len(a)-1):
    x1 = a[i]
    x2 = a[i-1]
    if x1.isupper() and x2.isupper():
        c += 1
    if x1.islower() and x2.islower():
        d += 1
    else:
        continue
for i in a:
    a.lower()
    if i in b:
        k1 += 1
    else:
        k2 += 1
print('Пар верхнего регистра:', c)
print('Пар нижнего регистра:', d)
print(f'В слове', k, 'букв,', k1, 'гласных,', k2, 'согласных.')