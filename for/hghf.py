a = input('vvedite')
b = 0
c = 0
for i in a:
    if int(i) % 2 == 0:
        b += 1
    else:
        c = 0
        print('b: %d, c: %d' % (b, c))