class Car:
    def print(self):
        print('Управляй мечтой')
    model = 'BMW'
    engine = 1.6
print(dir(Car))
ex = Car()
c = Car()
c.print()
print(c.model)
d = Car()
d.print()
print(d.engine)
e = Car()
e.engine = 2.0
e.print()
print(e.engine)


# c.model('BMW')