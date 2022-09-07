class Myclass():

    TOTAL_OBJECTS = 0

    def __init__(self):
        Myclass.TOTAL_OBJECTS = Myclass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print('Total objects: ', cls.TOTAL_OBJECTS)
#Создаем обьекты
my_obj1 = Myclass()
my_obj2 = Myclass()
my_obj3 = Myclass()
#Вызываем classmethod
Myclass.total_objects()

class ChildClass(Myclass):
    TOTAL_OBJECTS = 0

    def __init__(self):
        ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS + 1

    pass
my_obj1 = ChildClass()
ChildClass.total_objects()