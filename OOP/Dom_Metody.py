#Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса
class Example:
    def func(self):
        self.a = 5
        print (self.a)
    def func1(self,d,f):
        self.d = d
        self.f = f
        return self.d * self.f

ex = Example()
ex.func()
print(ex.func1(3,8))

class User():
    @staticmethod
    def is_adult(age):
        if age > 18:
            return ('Доступ Разрешен')
        else:
            return ('Доступ Запрещен')


class child_User(User):
    pass
print(User.is_adult(32))
print(child_User.is_adult(13))

class Home():
    table = 2
    @classmethod
    def room(cls):
        print('Столов в комнате: ', cls.table)
Home.room()