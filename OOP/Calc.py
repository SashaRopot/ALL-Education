#Калькулятор. Создайте класс, где реализованы функции(методы) математических операций.
#А также функция, для ввод данных.


class Calc:
    def __init__(self):
        self.vvod()
    def plus(self):
        return self.a + self.b
    def minu(self):
        return self.a - self.b
    def deje(self):
        if self.b == 0:
            return 'error'
        else:
            return self.a/self.b
    def umn(self):
        return self.a*self.b
    def vvod(self):
        self.a = int(input('Введите первое число: '))
        self.b = int(input('Введите второе число: '))

while True:
    ex = Calc()
    c = input('Введите операцию(+,-,*,/): ')
    if c == '+':
        print(ex.plus())
    elif c == '-':
        print(ex.minu())
    elif c == '*':
        print(ex.umn())
    elif c == 0:
        break
    else:
        print(ex.deje())