class Example:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def func(self):
        self.c = 5
        print(self.c)

    def func_1(self):
        return self.a + self.b

    def func_3(self):
        return self.t * self.r
ex = Example(5,6)
print(ex.a)
print(ex.func_1())
ex.func_1()
print(ex.func_3())