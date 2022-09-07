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
def ex(a,b):
    if a == 0 or b == 0:
        print('Выход из программы')
        return exit()
while True:
    choise = input('Какую операцию вы хотите совершить?(1-сложение, 2-разность, 3-умножение, 4-деление, 0-выход из программы): ')
    c = 'Введите первое число(0-выход из программы): '
    d = 'Введите второе число(0-выход из программы): '
    if choise == '1':
        a = float(input(c))
        b = float(input(d))
        ex(a,b)
        s = sum(a,b)
        print(f'Сумма чисел', a, 'и' , b,'равна', s)
    elif choise == '2':
        a = float(input(c))
        b = float(input(d))
        ex(a,b)
        s = difference(a,b)
        print(f'Разность чисел', a, 'и' , b,'равна', s)
    elif choise == '3':
        a = float(input(c))
        b = float(input(d))
        ex(a,b)
        s = multiplication(a,b)
        print(f'Произведение чисел', a, 'и' , b,'равно', s)
    elif choise == '4':
        a = float(input(c))
        b = float(input(d))
        ex(a,b)
        s = div(a,b)
        print(f'Деление чисел', a, 'и' , b,'равно', s)
    elif choise == '0':
        print('Выход из программы')
        exit()


