def func(a):
    c = 0
    b = 0
    while a>0:
        d = a % 10
        if d % 2 == 0:
            c += 1
        else:
            b += 1
        a = a // 10
     return 'Нечетных цифр: ', b
d = func(345)
print(type(d))
print(d)
# b=0
        # c=0
        # for i in args:
        #     if i.isalpha():
        #         b += len(i)
        #     if i.isdigit():
        #         c += 1