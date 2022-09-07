class Car:
    default_color = 'grey'
    default_weight = 2500
    def __init__(self, color, options):
        self.color = color
        self.options = options
    # def print(self):
    #     print('Управляй мечтой')
    # model = 'BMW'
    # engine = 1.6
car_object = Car('Black', 'Webasto')
print(dir(Car))
# c = Car()
# c.print()
# d = Car()
# d.print()
# e = Car()
# e.print()
print(car_object.default_weight)
print(car_object.options)


