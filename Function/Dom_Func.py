#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
#Если список, то посчитать кол-во букв и чисел в нём.
#Число – кол-во нечётных цифр.
#Строка – количество букв.
#Сделать проверку со всеми этими случаями.
def func(a):
    if isinstance(a,tuple):
        a = list(a)
        b = 0
        for i in a:
            if isinstance(i, str):
                b += len(i)
        return b
    if isinstance(a,list):
        k = 0
        c = 0
        for i in a:
            if isinstance(i,int):
                c += 1
            else:
                k+=len(i)
        return ('Букв:', k, 'Чисел:', c)
    if isinstance(a,int):
        c = 0
        b = 0
        while a > 0:
            d = a % 10
            if d % 2 == 0:
                c += 1
            else:
                b += 1
            a = a // 10
        return 'Нечетных цифр: ', b
    if isinstance(a,str):
        return len([i for i in a if i.isalpha()])
d = func(33546)
print(d)