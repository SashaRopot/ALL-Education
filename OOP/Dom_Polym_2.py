class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a}*{self.b}'

    def get_area(self):
        return self.a * self.b


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a}*{self.a}'

    def get_area(self):
        return self.a ** 2


sq1 = Square(5)
sq2 = Square(7)


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle radius = {self.r}'

    def get_area(self):
        return 3.14 * self.r ** 2


cir1 = Circle(3)
cir2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area())
