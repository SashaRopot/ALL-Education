a = 7
if a>0: #может быть любое условие
    b = a + 4
    if b == 3:
        print(3)
    elif b>0:
        print(b)
    else:
        print('hello')
elif a == 0:
    print('0')
elif a<0:
    print('a<0')
else: #никогда не пишем условие
    print('else')
