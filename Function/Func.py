#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
#Если список, то посчитать кол-во букв и чисел в нём.
#Число – кол-во нечётных цифр.
#Строка – количество букв.
#Сделать проверку со всеми этими случаями.


def func(*args,**kwargs):
    if isinstance(a,tuple):
        return len(a)
    # if isinstance(a,int):
    #     a = list()
    #
    #     for i in a:
    #         if int(i) % 2 == 0:
    #             b += 1
    #     return b
    if isinstance(a,str):
        return len([i for i in a if i.isalpha()])
print(type(func((45243, 'sdfg', 'sdgsf', 234))))
