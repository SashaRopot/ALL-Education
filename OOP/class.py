class Myclass():
    @staticmethod
    def staticmethod():
        print('static method called')

class children_My_class(Myclass):
    pass


my_obj = Myclass()
my_obj.staticmethod()
my_obj_1 = children_My_class()
my_obj_1.staticmethod()