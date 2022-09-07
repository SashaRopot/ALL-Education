class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):  # get_rect_area
        return self.a * self.b


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)


# print(rect1.get_rect_area(), rect2.get_rect_area())


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):  # get_sq_area
        return self.a ** 2


sq1 = Square(5)
sq2 = Square(7)


# print(sq1.get_sq_area(), sq2.get_sq_area())


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):  # get_circle_area
        return 3.14 * self.r ** 2


cir1 = Circle(3)
cir2 = Circle(2)
# print(cir1.get_circle_area(),cir2.get_circle_area())


figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure.get_area())
    # if isinstance(figure, Square):
    #     print(figure.get_sq_area())
    # elif isinstance(figure, Circle):
    #     print(figure.get_circle_area())
    # else:
    #     print(figure.get_rect_area())
