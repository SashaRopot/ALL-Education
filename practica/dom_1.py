# С клавиатуры вводится 7-значное число. Если четных цифр в нем больше, чем нечетных,
# то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 цифры.
a = list(input('Введите число из 7 цифр: '))
print(a)
b = 0
c = 0
d = 0
e = int(a[0])
f = int(a[2])
g = int(a[5])
for i in a:
    d += int(i)
    if int(i) % 2 == 0:
        b +=1
    else:
        c +=1
if b > c:
    print(d)
else:
    print(e*f*g)
print(type(a))