a = str(input('Введите два числа через пробел: '))
b = str(int(a[0]) - int(a[2]))

f = open('input.txt', 'w')
f.write(a)
f.close()
f = open('output.txt', 'w')
f.write(b)
f.close()
print(b)
print(type(b))


# g = open('input.txt', 'w')
# print(g.readlines())
# g.close()
#
