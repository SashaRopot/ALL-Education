#Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
#Количество введенных чисел в список и искомая цифра задаются с клавиатуры. Числа выбираются рандомно.
import random
a1 = int(input('Введите количество чисел: '))
b = input('Введите искомую цифру: ')
a = random.sample(range(30),a1)
a2 = ' '.join(map(str, a))
c = 0
for i in a2:
    if i == b and i.isdigit():
        c += 1
    else:
        continue
print(a)
print(f'В списке цифра', b, 'встречается', c, 'раз')