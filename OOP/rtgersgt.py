class Example:
    def __init__(self):
        self.vvod()

    def dlina(self):
        return len(self.a)

    def proizv(self):
        a = 'аоуэыяёюеиeyuioa'
        g = 0
        s = 0
        p = 0
        sogl = []
        glas = []
        if type(self.a) == str:
            for i in self.a:
                if i in a:
                    g += 1
                    glas.append(i)
                else:
                    s += 1
                    sogl.append(i)
            if g * s <= ex.dlina():
                print(glas)
            else:
                print(sogl)
        elif type(self.a) == int:
            for i in str(self.a):
                if int(i) % 2 == 0:
                    p += int(i)
                print(p * ex.dlina())
    def vvod(self):
        self.a = input('Vvedite: ')
ex = Example()
print(ex.dlina())
print(ex.proizv())
