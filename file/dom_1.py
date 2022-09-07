#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность
a = (input('Введите два числа через пробел: ').split())
b = str(int(a[0]) - int(a[1]))
a1 = ' '.join(map(str,a))
# print(type(a1))
# print(b)
f = open('input.txt', 'w')
f.write(a1)
f.close()
f = open('output.txt', 'w')
f.write(b)
f.close()



# f = open('input.txt', 'r')
# for i in f:
#     print(i)
# f.close()
# f = open('output.txt', 'w')
# print(f.write(''))
# f.close()