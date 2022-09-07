# необходимо вывести все отрицательные числа. -5 и 3, на экране вывелось -4,-3,-2,-1
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# while a > b or b > a:
#     if b < -1:
#         b += 1
#         print(b)
#     elif a < -1:
#         a += 1
#         print(a)
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# for i in range(a,b):
#     while int(i) < b and i < -1:
#      i +=1
#      print(i)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while a < -1 and a < b:
    a += 1
    print(a)
if a > b and b > -1:
    print('нет отрицательных чисел в заданном диапазоне')

else:
    while b < -1 and b < a:
        b +=1
        print(b)
if a < b and a > 0:
    print('нет отрицательных чисел в данном диапазоне')
if a == b:
    print('нет диапазона')

