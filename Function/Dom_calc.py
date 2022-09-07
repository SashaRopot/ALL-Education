#Простейший калькулятор c введёнными двумя числами вещественного типа.
#Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
#Обработать ошибку: “Деление на ноль”
#Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def sum(a,b):
    return a+b
def difference(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def div(a,b):
    try:
        return division(a,b)
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

choise = input('Какую операцию вы хотите совершить?(1-сложение, 2-разность, 3-умножение, 4-деление, 0-выход из программы): ')
if choise == '1':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    s = sum(a,b)
    print(f'Сумма чисел', a, 'и' , b,'равна', {s})
if choise == '2':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    s = difference(a,b)
    print(f'Разность чисел', a, 'и' , b,'равна', {s})
if choise == '3':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    s = multiplication(a,b)
    print(f'Произведение чисел', a, 'и' , b,'равно', {s})
if choise == '4':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    s = div(a,b)
    print(f'Деление чисел', a, 'и' , b,'равно', {s})

if choise == '0':
    print('Выход из программы')
    exit()

